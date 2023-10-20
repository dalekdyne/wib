from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from bson.objectid import ObjectId as BsonObjectId


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class Podcast(BaseModel):
    _id: PydanticObjectId
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    language: Optional[str]
    rating: Optional[str]
    artwork: Optional[str]
    website: Optional[str]
    creator: Optional[str]
    feed_url: Optional[str]
    user_id: Optional[str]
    email: Optional[str]
    donations_url: Optional[str]
    org_id: Optional[str] = None
    iheart: Optional[bool] = False
    podcastindex: Optional[bool] = False
    spotify: Optional[bool] = False
    apple: Optional[bool] = False
    youtube: Optional[bool] = False
    soundcloud: Optional[bool] = False


class PodcastEpisode(BaseModel):
    _id: PydanticObjectId
    title: Optional[str]
    streams: Optional[str]
    description: Optional[str]
    release_date: Optional[datetime]
    type: Optional[str]
    rating: Optional[str]
    artwork: Optional[str]
    audio: Optional[str]
    status: Optional[str]
    transcription: Optional[str]
    transcription_status: Optional[str] = "none"
    podcast_id: Optional[str]
    user_id: Optional[str]
