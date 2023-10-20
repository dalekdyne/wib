from core.cognito import CognitoClient


class AuthService:
    def __init__(self):
        self.cognito = CognitoClient()

    def get_user(self, access_token):
        return self.cognito.get_user(access_token)

    def get_user_by_username(self, username):
        return self.cognito.get_user_by_username(username)

    def get_user_by_email(self, email):
        return self.cognito.get_user_by_email(email)

    def sign_up(self, username, password, email):
        return self.cognito.sign_up(username, password, email)

    def confirm_sign_up(self, username, confirmation_code):
        return self.cognito.confirm_sign_up(username, confirmation_code)

    def initiate_auth(self, username, password):
        return self.cognito.initiate_auth(username, password)

    def change_password(self, access_token, previous_password, proposed_password):
        return self.cognito.change_password(
            access_token, previous_password, proposed_password
        )

    def forgot_password(self, username):
        return self.cognito.forgot_password(username)

    def confirm_forgot_password(self, username, confirmation_code, password):
        return self.cognito.confirm_forgot_password(
            username, confirmation_code, password
        )
