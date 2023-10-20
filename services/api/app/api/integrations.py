from fastapi import APIRouter, HTTPException
from infra.mongodb.podcast.repository import PodcastRepository
from integrations.podcastindex import PodcastIndex

router = APIRouter(tags=["integrations"])

pi = PodcastIndex()


@router.get(path="/integrations/podcastindex/{id}")
async def submit_podcastindex(id: str):

    podcast = PodcastRepository.get_by(id)
    if podcast is not None:
        result = pi.submit_podcast(podcast)
        if result is False:
            raise HTTPException(
                status_code=500,
                detail="Something went wrong when submitting podcast to PodcastIndex",
            )
        else:
            PodcastRepository.update(id, {"podcastindex": True})
            return {"status": "success"}
    else:
        raise HTTPException(status_code=404, detail="Podcast not found")
