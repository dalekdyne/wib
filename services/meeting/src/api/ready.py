from fastapi import APIRouter, HTTPException
from core.ms import MS100Client

router = APIRouter(tags=["ready"])


@router.get("/ready")
async def ready():
    try:
        client = MS100Client()
        client.check_connection()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
