from core.ms import MS100Client


class MeetingService:
    def __init__(self, client: MS100Client):
        self.client = client

    def create_meeting(self, room_id: str, user_role: str):
        """
        Create a meeting room
        :param room_id: The room ID
        :param user_role: The user role
        :return: The room ID
        """
        room_name = f"Meeting Room {room_id}"
        self.client.create_room(room_id, room_name)
        token = self.client.generate_token(room_id, user_role)
        return token

    def get_meeting_token(self, room_id: str, user_role: str):
        """
        Get a meeting token
        :param room_id: The room ID
        :param user_role: The user role
        :return: The JWT token
        """
        token = self.client.generate_token(room_id, user_role)
        return token
