from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from api.health import router as health_router
from api.userdata import router as user_router
from api.ready import router as ready_router

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="Userdata Service")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(ready_router)
app.include_router(user_router)
