from fastapi import APIRouter, Depends

from app.podcast import model
from app.podcast.service import PodcastService

router = APIRouter(tags=["podcasts"])


@router.post(path="/podcast/")
async def create_podcast(
    podcast: model.Podcast,
    service: PodcastService = Depends(),
):
    return service.create(podcast)


@router.patch(path="/podcast/{id}")
async def update_podcast(
    id: str,
    podcast: model.Podcast,
    service: PodcastService = Depends(),
):
    return service.update(id, podcast)


@router.delete(
    path="/podcast/{id}",
)
async def delete_podcast(
    id: str,
    service: PodcastService = Depends(),
):
    return service.delete_by(id)


@router.get(
    path="/podcast/{id}",
)
async def get_podcast(
    id: str,
    service: PodcastService = Depends(),
):
    return service.get_by(id)


@router.get(path="/podcast/")
async def get_all_podcasts(
    user_id: str,
    service: PodcastService = Depends(),
):
    return service.get_all_by(user_id)


@router.post(path="/podcast/publish/")
async def publish_podcast(
    id: str,
    user_id: str,
    service: PodcastService = Depends(),
):
    return service.publish_podcast_by(user_id, id)
