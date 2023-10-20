import os


class ConfigParams:
    MONGODB_HOST = os.getenv("MONGODB_HOST", "mongodb://localhost:27017")
    MONGODB_DBNAME = os.getenv("MONGODB_DBNAME", "podhustlr-main")
    PODCASTINDEX_API_KEY = os.getenv("PODCASTINDEX_API_KEY", "")
    PODCASTINDEX_API_SECRET = os.getenv("PODCASTINDEX_API_SECRET", "")
    MS100_WEBHOOK_HEADER_SECRET = os.getenv("MS100_WEBHOOK_HEADER_SECRET", "")
