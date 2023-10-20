from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["health"])


@router.get("/health")
async def health():
    try:
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
