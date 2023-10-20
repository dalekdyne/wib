import boto3
from config import Config


class CognitoClient:
    def __init__(self):
        self.region = Config.COGNITO_REGION_NAME
        self.user_pool_id = Config.COGNITO_USER_POOL_ID
        self.client_id = Config.COGNITO_APP_CLIENT_ID
        self.client = boto3.client("cognito-idp", region_name=self.region)

    def get_user(self, access_token):
        return self.client.get_user(AccessToken=access_token)

    def get_user_by_username(self, username):
        return self.client.admin_get_user(
            UserPoolId=self.user_pool_id, Username=username
        )

    def get_user_by_email(self, email):
        return self.client.list_users(
            UserPoolId=self.user_pool_id, Filter=f'email = "{email}"'
        )

    def sign_up(self, username, password, email):
        return self.client.sign_up(
            ClientId=self.client_id,
            Username=username,
            Password=password,
            UserAttributes=[{"Name": "email", "Value": email}],
        )

    def confirm_sign_up(self, username, confirmation_code):
        return self.client.confirm_sign_up(
            ClientId=self.client_id,
            Username=username,
            ConfirmationCode=confirmation_code,
        )

    def initiate_auth(self, username, password):
        return self.client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": username, "PASSWORD": password},
            ClientId=self.client_id,
        )

    def sign_out(self, access_token):
        return self.client.global_sign_out(AccessToken=access_token)

    def change_password(self, access_token, previous_password, proposed_password):
        return self.client.change_password(
            PreviousPassword=previous_password,
            ProposedPassword=proposed_password,
            AccessToken=access_token,
        )

    def forgot_password(self, username):
        return self.client.forgot_password(ClientId=self.client_id, Username=username)

    def confirm_forgot_password(self, username, confirmation_code, password):
        return self.client.confirm_forgot_password(
            ClientId=self.client_id,
            Username=username,
            ConfirmationCode=confirmation_code,
            Password=password,
        )
