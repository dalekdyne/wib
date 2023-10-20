from fastapi import APIRouter, HTTPException

from app.userdata.service import UserService


router = APIRouter(tags=["ready"])
user_service = UserService()


@router.get("/ready")
async def health(username: str, user_pool_id: str):
    try:
        user = user_service.get_user(username, user_pool_id)
        if user is not None:
            return {"status": "ok"}
        else:
            return {"status": "not available"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
