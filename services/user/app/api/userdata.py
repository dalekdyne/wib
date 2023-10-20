from fastapi import APIRouter, HTTPException

from app.userdata.service import UserService

router = APIRouter(tags=["userdata"])
user_service = UserService()


@router.post("/disable")
async def disable(username: str, user_pool_id: str):
    try:
        return user_service.get_user(username, user_pool_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/enable")
async def enable(username: str, user_pool_id: str):
    try:
        return user_service.enable_user(username, user_pool_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/delete")
async def delete(access_token: str):
    try:
        return user_service.delete_user(access_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
