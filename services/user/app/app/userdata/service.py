from infra.cognito.client import CognitoClient


class UserService:
    def __init__(self):
        self.cognito = CognitoClient()

    def get_user(self, username: str, user_pool_id):
        return self.cognito.get_user(username, user_pool_id)

    def delete_user(self, access_token: str):
        return self.cognito.delete_user(access_token)

    def disable_user(self, username: str, user_pool_id):
        return self.cognito.disable_user(user_pool_id, username)

    def enable_user(self, username: str, user_pool_id):
        return self.cognito.enable_user(user_pool_id, username)
