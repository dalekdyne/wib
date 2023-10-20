from fastapi.logger import logger
from db import interviewdb
from models.interview import Interview


class MS100_WebhookService:
    def __init__(self):
        pass

    def handle_event(self, event):
        # For a list of all events see https://www.100ms.live/docs/server-side/v2/introduction/webhook#list-of-events
        if event["type"] == "recording.success":
            logger.info("Recording success: ", event)
            # create new empty dict
            interview = {
                "title": event["data"]["room_name"]
                + " - "
                + event["data"]["session_id"],
                "date": event["timestamp"],
                "recording_uri": event["data"]["location"],
                "room_id": event["data"]["room_id"],
                "session_id": event["data"]["session_id"],
            }
            # TODO: add a new episode instead of a new interview
            interview = Interview(**interview)
            interviewdb.create_interview(interview)
        elif event["type"] == "recording.failed":
            print("Recording failed: ", event)
            return
