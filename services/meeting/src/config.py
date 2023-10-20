import os


class Config:
    MS100_APP_KEY = os.environ.get("MS100_APP_KEY")
    MS100_APP_SECRET = os.environ.get("MS100_APP_SECRET")
    MS100_API_URL = os.environ.get("MS_100_API_URL")
    MS100_ROOM_TEMPLATE = os.environ.get("MS_100_ROOM_TEMPLATE")
    MS100_S3_BUCKET = os.environ.get("MS_100_S3_BUCKET")
    MS100_WEBHOOK_SECRET = os.environ.get("MS_100_WEBHOOK_SECRET")
    MS100_AWS_ACCESS_KEY_ID = os.environ.get("MS_100_AWS_ACCESS_KEY_ID")
    MS100_AWS_SECRET_ACCESS_KEY = os.environ.get("MS_100_AWS_SECRET_ACCESS_KEY")
    MS100_AWS_REGION = os.environ.get("MS_100_AWS_REGION")
    COGNITO_REGION_NAME = os.environ.get("COGNITO_REGION_NAME")
    COGNITO_USER_POOL_ID = os.environ.get("COGNITO_USER_POOL_ID")
    COGNITO_APP_CLIENT_ID = os.environ.get("COGNITO_APP_CLIENT_ID")
