import pymongo
from fastapi.logger import logger

from config import ConfigParams


class Database:
    def __init__(self):
        self.db_client = pymongo.MongoClient(
            ConfigParams.MONGODB_HOST, serverSelectionTimeoutMS=100000
        )
        self.db = self.db_client[ConfigParams.MONGODB_DBNAME]
        self.col_podcasts = self.db["podcasts"]
        self.col_episodes = self.db["episodes"]


logger.info("Connecting to MongoDB...")
try:
    database = Database()
except pymongo.errors.ServerSelectionTimeoutError:
    logger.error("Could not connect to MongoDB.")
    exit(1)
