from fastapi import APIRouter, HTTPException

from core.smtp import MailClient

router = APIRouter(tags=["ready"])


@router.get("/ready")
async def ready():
    try:
        for client in MailClient.__subclasses__():
            client()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
