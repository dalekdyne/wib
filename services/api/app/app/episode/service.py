"""
Module service is responsible for providing the application with a service layer for
episode management.
"""
import logging

from fastapi import HTTPException

from app.episode.model import PodcastEpisode
from core.helpers import parse_json
from infra.mongodb.episode.repository import EpisodeRepository


class EpisodeService:
    """
    Class EpisodeService handles the flow of an episode
    """

    def __init__(self):
        self.repository = EpisodeRepository()

    def create(self, episode: PodcastEpisode):
        """
        create takes an episode and creates one in the database
        """

        result = self.repository.create(episode)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when creating episode"
            )

        return {"id": result}

    def update(self, _id: str, episode: PodcastEpisode):
        """
        update takes an id and an episode and updates it in the database
        """
        result = self.repository.update(_id, episode)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when updating episode"
            )

        return {"id": result}

    def delete_by(self, _id: str):
        """
        delete_by takes an id and deletes an episode
        """
        result = self.repository.delete_by(_id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when deleting episode"
            )

        return {"id": result}

    def get_by(self, _id: str):
        """
        get_by takes an id and fetches an episode
        """
        try:
            result = self.repository.get_by(_id)
        except Exception as exception:
            logging.error(str(exception))
            raise HTTPException(status_code=500, detail=str(exception)) from exception

        if result is None:
            raise HTTPException(status_code=404, detail="Episode not found.")

        return parse_json(result)

    def get_all_for_user_by_podcast_id(self, user_id: str, podcast_id: str):
        """
        get_all_for_user_by_podcast_id fetches all episodes for a user and podcast
        """
        result = self.repository.get_all_for_user_by_podcast(user_id, podcast_id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when getting episodes"
            )

        return parse_json(result)

    def get_episode_count_for_user_and_podcast(self, user_id: str, podcast_id: str):
        """
        get_episode_count_for_user_and_podcast fetches the episode count for a user and podcast
        """
        try:
            result = self.repository.get_episode_count_for_user_podcast(
                user_id, podcast_id
            )
        except Exception as e:
            logging.error(str(e))
            raise HTTPException(status_code=500, detail=str(e))

        return {"count": result}

    def get_streams_for_user_and_podcast(self, user_id: str, podcast_id: str):
        """
        get_streams_for_user_and_podcast fetches the streams for a user and podcast
        """
        try:
            result = self.repository.get_streams_for_user_podcast(user_id, podcast_id)
        except Exception as e:
            logging.error(str(e))
            raise HTTPException(status_code=500, detail=str(e))

        return {"streams": result}

    def get_all_for_user(self, user_id: str):
        """
        get_all_for_user fetches all episodes for a user
        """
        result = self.repository.get_all_for_user(user_id)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Something went wrong when getting episodes"
            )

        return parse_json(result)
