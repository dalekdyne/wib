from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    access_token: str


class UserChangePassword(BaseModel):
    access_token: str
    previous_password: str
    proposed_password: str


class UserForgotPassword(BaseModel):
    username: str
    confirmation_code: str
    password: str
