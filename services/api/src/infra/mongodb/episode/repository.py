from bson.objectid import ObjectId
from fastapi.logger import logger

from app.episode.model import PodcastEpisode
from infra.mongodb.db import Database


class EpisodeRepository:
    def __init__(self):
        self.dbClient = Database()
        pass

    def create(self, episode: PodcastEpisode):
        w = None

        try:
            w = self.dbClient.col_episodes.insert_one(episode.dict()).inserted_id
        except Exception as e:
            logger.error("Error inserting: ", e)

        # Required str() becasue insert_one returns a <class 'bson.objectid.ObjectId'>
        return str(w)

    def update(self, id: str, episode: PodcastEpisode):
        _id = ObjectId(id)
        try:
            if isinstance(episode, dict):
                self.dbClient.col_episodes.update_one({"_id": _id}, {"$set": episode})
            else:
                # update_episode can be used outside of API so we need to check if the episode has a podcast_id
                if episode.podcast_id is not None:
                    self.dbClient.col_episodes.update_one(
                        {"_id": _id}, {"$set": episode.dict(exclude_unset=True)}
                    )
        except Exception as e:
            logger.error("Error updating:", e)

        return id

    def delete_by(self, id: str):
        _id = ObjectId(id)
        try:
            self.dbClient.col_episodes.delete_one({"_id": _id})
        except Exception as e:
            logger.error("Error deleting:", e)

        return id

    def get_by(self, id: str):
        _id = ObjectId(id)
        f = None
        try:
            f = self.dbClient.col_episodes.find_one({"_id": _id})
        except Exception as e:
            logger.error("Error finding:", e)

        return f

    def get_all_for_user_by_podcast(self, user_id: str, podcast_id: str):
        f = None
        res = []
        try:
            f = self.dbClient.col_episodes.find(
                {"user_id": user_id, "podcast_id": podcast_id}
            )

            for doc in f:
                res.append(doc)
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    def get_episode_count_for_user_podcast(self, user_id: str, podcast_id: str):
        res = 0
        try:
            f = None
            f = self.dbClient.col_episodes.find(
                {"user_id": user_id, "podcast_id": podcast_id}
            )

            if f is not None:
                for doc in f:
                    res += 1
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    def get_streams_for_user_podcast(self, user_id: str, podcast_id: str):
        res = 0
        try:
            f = None
            f = self.dbClient.col_episodes.find(
                {"user_id": user_id, "podcast_id": podcast_id}
            )

            if f is not None:
                for doc in f:
                    # Increase result with value of streams
                    res += int(doc["streams"])
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    def get_all_for_user(self, user_id: str):
        res = []
        try:
            f = None
            f = self.dbClient.col_episodes.find({"user_id": user_id})
            if f is not None:
                for doc in f:
                    res.append(doc)
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    # Mainly used in the analytics scheduler.
    def get_all_episode_ids(self):

        res = []
        try:
            f = None
            f = self.dbClient.col_episodes.find()

            if f is not None:
                for doc in f:
                    res.append(doc["_id"])
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    def get_all_episodes_by_podcast_id(self, podcast_id: str):
        res = []
        try:
            f = None
            f = self.dbClient.col_episodes.find({"podcast_id": podcast_id})

            if f is not None:
                for doc in f:
                    res.append(doc)
        except Exception as e:
            logger.error("Error finding:", e)

        return res

    def get_all_episodes_by_user_id(self, user_id):
        res = []
        try:
            f = None
            f = self.dbClient.col_episodes.find({"user_id": user_id})

            if f is not None:
                for doc in f:
                    res.append(doc)
        except Exception as e:
            logger.error("Error finding:", e)

        return res
