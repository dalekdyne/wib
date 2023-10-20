from pydantic import BaseModel


class Confirmation(BaseModel):
    code: str
    username: str
