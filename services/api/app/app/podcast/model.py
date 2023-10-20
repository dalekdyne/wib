from typing import List, Optional

from bson.objectid import ObjectId as BsonObjectId
from fastapi_users_db_mongodb import UUID4
from podgen import Category, Person
from podgen import Podcast as PodGenPodcast
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
    user_id: Optional[UUID4]
    email: Optional[str]
    iheart: Optional[bool] = False
    podcastindex: Optional[bool] = False
    spotify: Optional[bool] = False
    apple: Optional[bool] = False
    youtube: Optional[bool] = False
    soundcloud: Optional[bool] = False


def createPodGenPodcastFrom(podcast: Podcast) -> PodGenPodcast:
    # Create podcast object
    p = PodGenPodcast()
    p.name = podcast["title"]
    p.description = podcast["description"]
    p.authors = [Person(podcast["creator"], podcast["email"])]
    p.owner = p.authors[0]
    p.language = podcast["language"]
    p.category = (
        Category(podcast["category"])
        if podcast["category"] != ""
        else Category("Leisure")
    )
    p.image = podcast["artwork"]
    # Add podcast website if not empty or add https://podbeam.io
    p.website = podcast["website"] if podcast["website"] != "" else "https://podbeam.io"
    p.explicit = podcast["rating"] == "Explicit"
    p.generator = "Podbeam"

    return p
