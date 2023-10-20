import os


class Config:
    COGNITO_REGION_NAME = os.environ.get("COGNITO_REGION_NAME", "us-east-1")
    COGNITO_USER_POOL_ID = os.environ.get("COGNITO_USER_POOL_ID")
    COGNITO_APP_CLIENT_ID = os.environ.get("COGNITO_APP_CLIENT_ID")
