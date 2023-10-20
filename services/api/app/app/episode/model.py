from datetime import datetime
from typing import Optional

import pytz
from bson.objectid import ObjectId as BsonObjectId
from fastapi_users_db_mongodb import UUID4
from podgen import Episode as PodGenEpisode
from podgen import Media
from pydantic import BaseModel


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return str(v)


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
    video: Optional[str]
    status: Optional[str]
    podcast_id: Optional[str]
    user_id: Optional[UUID4]


def createPodGenEpisodeFrom(episode: PodcastEpisode) -> PodGenEpisode:
    # Get UTC timezone
    timezone = pytz.timezone("UTC")

    e = PodGenEpisode()
    # Adding an episode id. If the id is missing,
    # then we cannot recreate the XML without breaking user experience.
    # This breaks if the id is not a string.

    e.id = str(episode["_id"])
    e.title = episode["title"]
    e.image = episode["artwork"]
    e.subtitle = episode["description"][:100]
    e.summary = episode["description"][:500]
    e.long_summary = episode["description"]
    e.media = Media(episode["audio"])
    e.explicit = episode["rating"] == "Explicit"
    e.publication_date = timezone.localize(episode["release_date"])

    return e
