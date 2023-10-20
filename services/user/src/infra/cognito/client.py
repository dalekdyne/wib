import boto3
import logging

from config.config import Config

logger = logging.getLogger(__name__)


class CognitoClient:
    def __init__(self):
        self.region = Config.COGNITO_REGION_NAME
        self.user_pool_id = Config.COGNITO_USER_POOL_ID
        self.client_id = Config.COGNITO_APP_CLIENT_ID
        self.client = boto3.client("cognito-idp", region_name=self.region)

    def get_user(self, username: str, user_pool_id: str):
        return self.client.admin_get_user(
            UserPoolId=user_pool_id,
            Username=username
        )

    def delete_user(self, access_token: str):
        return self.client.delete_user(AccessToken=access_token)

    def disable_user(self, username: str, user_pool_id: str):
        return self.client.admin_disable_user(
            UserPoolId=user_pool_id,
            Username=username
        )

    def enable_user(self, username: str, user_pool_id: str):
        return self.client.admin_enable_user(
            UserPoolId=user_pool_id,
            Username=username
        )
