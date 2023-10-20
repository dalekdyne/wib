from fastapi_cloudauth.cognito import Cognito
from pydantic import BaseModel

from config import Config

class AccessUser(BaseModel):
    sub: str

auth = Cognito(
    region=Config.COGNITO_REGION_NAME,
    userPoolId=Config.COGNITO_USER_POOL_ID,
    client_id=Config.COGNITO_APP_CLIENT_ID,
)

current_user = auth.claim(AccessUser)
