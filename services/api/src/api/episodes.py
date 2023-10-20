from fastapi import APIRouter, Depends

from app.episode import model
from app.episode.service import EpisodeService

router = APIRouter(tags=["episodes"])


@router.post(path="/episode/")
async def create_episode(
    podcast_episode: model.PodcastEpisode,
    service: EpisodeService = Depends(),
):
    return service.create(podcast_episode)


@router.patch(path="/episode/{id}")
async def update_episode(
    id: str,
    podcast_episode: model.PodcastEpisode,
    service: EpisodeService = Depends(),
):
    return service.update(id, podcast_episode)


@router.delete(
    path="/episode/{id}",
)
async def delete_episode(id: str, service: EpisodeService = Depends()):
    return service.delete_by(id)


@router.get(
    path="/episode/{id}",
)
async def get_episode(id: str, service: EpisodeService = Depends()):
    return service.get_by(id)


@router.get(path="/episode/podcast/{id}")
async def get_all_episodes_by_podcast(
    id: str, user_id: str, service: EpisodeService = Depends()
):
    return service.get_all_for_user_by_podcast_id(user_id, id)






@router.get(path="/episodes/")
async def get_all_episodes_by_user(user_id: str, service: EpisodeService = Depends()):
    service.get_all_for_user(user_id)
