import jwt
import uuid
import datetime
import requests
import logging

from config import Config


class MS100Client:
    def __init__(self):
        self.app_access_key = Config.MS100_APP_KEY
        self.app_secret = Config.MS100_APP_SECRET
        self.api_url = Config.MS100_API_URL
        self.room_template = Config.MS100_ROOM_TEMPLATE
        self.s3_bucket = Config.MS100_S3_BUCKET
        self.webhook_secret = Config.MS100_WEBHOOK_SECRET
        self.aws_access_key_id = Config.MS100_AWS_ACCESS_KEY_ID
        self.aws_secret_access_key = Config.MS100_AWS_SECRET_ACCESS_KEY
        self.aws_region = Config.MS100_AWS_REGION

    def check_connection(self):
        """
        Check if the connection to the MS100 API is working
        :return: True if the connection is working, False otherwise
        """
        try:
            response = requests.get(self.api_url + "/rooms")
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            logging.error(e)
            return False

    def generate_token(self, room_id, user_role):
        """
        Generate a JWT token for the user to join the meeting
        :param room_id: The room ID
        :param user_role: The user role
        :return: The JWT token
        """
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=3600)
        now = datetime.datetime.utcnow()
        payload = {
            "access_key": self.app_access_key,
            "type": "app",
            "version": "2",
            "room_id": room_id,
            "user_id": str(uuid.uuid4()),
            "role": user_role,
            "jti": str(uuid.uuid4()),
            "exp": expires,
            "iat": now,
            "nbf": now,
        }
        token = jwt.encode(payload, self.app_secret, algorithm="HS256")
        return token

    def generate_mgmt_token(self):
        """
        Generate a JWT token for the management API
        :return: The JWT token
        """
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        now = datetime.datetime.utcnow()
        payload = {
            "access_key": self.app_access_key,
            "type": "management",
            "version": "2",
            "jti": str(uuid.uuid4()),
            "exp": expires,
            "iat": now,
            "nbf": now,
        }
        token = jwt.encode(payload, self.app_secret, algorithm="HS256")
        return token

    def create_room(self, room_name):
        """
        Create a room
        :param room_id: The room ID
        :param room_name: The room name
        :return: The room ID
        """
        token = self.generate_mgmt_token()
        template = self.room_template
        credentials = {
            "key": self.aws_access_key_id,
            "secret": self.aws_secret_access_key,
        }
        region = self.aws_region
        options = {
            "region": region,
        }
        upload_info = {
            "type": "s3",
            "location": self.s3_bucket,
            "credentials": credentials,
            "options": options,
        }
        recording_info = {"enabled": True, "upload_info": upload_info}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        data = {
            "name": room_name,
            "description": room_name,
            "template": template,
            "recording_info": recording_info,
            "region": "eu",
        }

        try:
            response = requests.post(
                self.api_url + "/rooms", headers=headers, json=data
            )
            response.raise_for_status()
            return response.json()["id"]
        except requests.exceptions.HTTPError as e:
            logging.error(e)
            return None
