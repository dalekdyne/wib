from bson.objectid import ObjectId
from fastapi.logger import logger

from app.podcast import model
from app.podcast.repository import Repository
from infra.mongodb.db import Database


class PodcastRepository(Repository):
    def __init__(self):
        self.dbClient = Database()
        pass

    def create(self, podcast: model.Podcast):
        w = None
        try:
            w = self.dbClient.col_podcasts.insert_one(podcast.dict()).inserted_id
        except Exception as e:
            logger.error("Error inserting: ", e)

        # Required str() becasue insert_one returns a <class 'bson.objectid.ObjectId'>
        return str(w)

    def update(self, id: str, podcast: model.Podcast):
        _id = ObjectId(
            id
        )  # Convert to ObjectId to use in update https://stackoverflow.com/questions/60547442/pymongo-update-one-not-updating-based-on-id
        try:
            if isinstance(podcast, dict):
                self.dbClient.col_podcasts.update_one({"_id": _id}, {"$set": podcast})
            else:
                self.dbClient.col_podcasts.update_one(
                    {"_id": _id}, {"$set": podcast.dict(exclude_unset=True)}
                )
        except Exception as e:
            logger.error("Error updating:", e)

        return id

    def delete_by(self, id: str):
        _id = ObjectId(
            id
        )  # Convert to ObjectId to use in update https://stackoverflow.com/questions/60547442/pymongo-update-one-not-updating-based-on-id
        try:
            self.dbClient.col_podcasts.delete_one({"_id": _id})
        except Exception as e:
            logger.error("Error deleting:", e)

        return id

    def get_by(self, id: str):
        _id = ObjectId(
            id
        )  # Convert to ObjectId to use in update https://stackoverflow.com/questions/60547442/pymongo-update-one-not-updating-based-on-id
        f = None
        try:
            f = self.dbClient.col_podcasts.find_one({"_id": _id})
        except Exception as e:
            logger.error("Error finding:", e)

        return f

    def get_all_for_user(self, user_id: str):
        f = None
        res = []
        try:
            f = self.dbClient.col_podcasts.find({"user_id": user_id})

            for doc in f:
                res.append(doc)
        except Exception as e:
            logger.error("Error finding:", e)

        return res
