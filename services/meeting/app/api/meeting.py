from fastapi import APIRouter, HTTPException, Depends
from app.meeting.service import MeetingService
from core.ms import MS100Client
from core.auth import current_user

client = MS100Client()
service = MeetingService(client=client)
router = APIRouter(tags=["meeting"])


@router.get(path="/meeting/token")
async def get_meeting_token(room_id: str, user_role: str, user: str = Depends(current_user)):
    """
    Get a meeting token
    :param room_id: The room ID
    :param user_role: The user role
    :return: The JWT token
    """
    try:
        token = service.get_meeting_token(room_id, user_role)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/meeting/create")
async def create_meeting(room_id: str, user_role: str, user: str = Depends(current_user)):
    """
    Create a meeting room
    :param room_id: The room ID
    :param user_role: The user role
    :return: The room ID
    """
    try:
        token = service.create_meeting(room_id, user_role)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
