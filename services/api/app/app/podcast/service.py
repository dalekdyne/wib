import os
from fastapi import HTTPException
from fastapi.logger import logger

from app.episode import model as episode_model
from app.podcast import model as podcast_model
from core.helpers import is_date_in_future, parse_json
from infra.mongodb.episode.repository import EpisodeRepository
from infra.mongodb.podcast.repository import PodcastRepository


class PodcastService:
    def __init__(self):
        self.repository = PodcastRepository()
        self.episodeRepository = EpisodeRepository()
        pass

    def create(self, podcast: podcast_model.Podcast):
        result = self.repository.create(podcast)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when creating podcast"
            )

        return {"id": result}

    def update(self, id: str, podcast: podcast_model.Podcast):
        result = self.repository.update(id, podcast)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when updating podcast"
            )

        return {"id": result}

    def delete_by(self, id: str):
        result = self.repository.delete_by(id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when deleting podcast"
            )

        return {"id": result}

    def get_by(self, id: str):
        result = self.repository.get_by(id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when getting podcast"
            )

        return parse_json(result)

    def get_all_by(self, user_id: str):
        result = self.repository.get_all_for_user(user_id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when getting podcasts"
            )

        return parse_json(result)

    def publish_podcast_by(self, user_id: str, id: str):
        # Fetch podcast data
        podcast = self.repository.get_by(id)  # Got a dict

        # Fetch episodes data for podcast
        episodes = self.episodeRepository.get_all_for_user_by_podcast(
            user_id, id
        )  # Got a list of dicts

        pgp = podcast_model.createPodGenPodcastFrom(podcast)

        for episode in episodes:
            pge = episode_model.createPodGenEpisodeFrom(episode)

            pgp.episodes.append(pge)

            # Updating episode status to published
            try:
                self.episodeRepository.update(
                    episode["_id"],
                    episode_model.PodcastEpisode(
                        title=episode.get("title"),
                        description=episode.get("description", ""),
                        streams=episode.get("streams", 0),
                        release_date=episode.get("release_date", ""),
                        type=episode.get("type", ""),
                        rating=episode.get("rating", ""),
                        artwork=episode.get("artwork", ""),
                        audio=episode.get("audio", ""),
                        # Scenario this if is useful:
                        # If the episode is scheduled to be published in the future, there is a job pending for it.
                        # Now, the user schedules another episode to be published sooner
                        # than the most far scheduled one.
                        # If we update the episode status to Published without checking,
                        # then we would be setting the status to Published even for episodes
                        # that are scheduled to be published in the future.
                        status="Scheduled"
                        if is_date_in_future(episode.get("release_date", ""))
                        else "Published",
                        podcast_id=str(episode.get("podcast_id", "")),
                        user_id=episode.get("user_id", ""),
                    ),
                )
            except Exception as e:
                logger.error("Error updating episode with id: ", episode["_id"], e)

            # Write podcast feed to file
            pgp.rss_file(id + "-rss.xml", minimize=True)

            # Store file to bucket and get url
            # TODO: do an RPC to a remote function that will upload the file to the bucket and return the url
            # maybe a lambda function?

            # Delete local file
            os.remove(id + "-rss.xml")

            # Update podcast with feed url
            try:
                self.repository.update(
                    id,
                    podcast_model.Podcast(
                        title=podcast["title"],
                        description=podcast["description"],
                        category=podcast["category"],
                        language=podcast["language"],
                        rating=podcast["rating"],
                        website=podcast["website"],
                        email=podcast["email"],
                        creator=podcast["creator"],
                        artwork=podcast["artwork"],
                        user_id=podcast["user_id"],
                        org_id=podcast["org_id"],
                    ),
                )
            except Exception as e:
                logger.error("Error updating podcast with id: ", id, e)

            return "OK"
