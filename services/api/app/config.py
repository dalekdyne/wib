import os


class ConfigParams:
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
    DATANASE_NAME = os.getenv("DATABASE_NAME", "getwib-api")
    PODCASTINDEX_API_KEY = os.getenv("PODCASTINDEX_API_KEY", "")
    PODCASTINDEX_API_SECRET = os.getenv("PODCASTINDEX_API_SECRET", "")
    MS100_WEBHOOK_HEADER_SECRET = os.getenv("MS100_WEBHOOK_HEADER_SECRET", "")
