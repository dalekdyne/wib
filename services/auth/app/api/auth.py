from fastapi import APIRouter, HTTPException

from app.auth.service import AuthService
from models.user import User, UserIn, UserOut, UserChangePassword, UserForgotPassword
from models.confirmation import Confirmation

router = APIRouter(tags=["auth"])
auth_service = AuthService()


@router.post("/sign-up")
async def sign_up(user: User):
    try:
        return auth_service.sign_up(user.username, user.password, user.email)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/confirm-sign-up")
async def confirm_sign_up(confirmation: Confirmation):
    try:
        return auth_service.confirm_sign_up(confirmation.username, confirmation.code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sign-in")
async def sign_in(user: UserIn):
    try:
        return auth_service.initiate_auth(user.username, user.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sign-out")
async def sign_out(user: UserOut):
    try:
        return auth_service.sign_out(user.access_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/change-password")
async def change_password(user: UserChangePassword):
    try:
        return auth_service.change_password(
            user.access_token, user.previous_password, user.proposed_password
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/forgot-password")
async def forgot_password(username: str):
    try:
        return auth_service.forgot_password(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/confirm-forgot-password")
async def confirm_forgot_password(user: UserForgotPassword):
    try:
        return auth_service.confirm_forgot_password(
            user.username, user.confirmation_code, user.password
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
