from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from api import (
    podcasts,
    episodes,
)

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

description = """
Podbeam API helps you do awesome stuff with podcasts. 🚀

## Podcasts

* **Podcasts** - Manage podcasts

## Episodes

* **Episodes** - Manage episodes
"""

tags_metadata = [
    {"name": "episodes", "description": "Operations regarding episodes."},
    {"name": "podcasts", "description": "Operations regarding podcasts."},
]

app = FastAPI(
    title="Podbeam API",
)

# Configure CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Podcast management router
app.include_router(podcasts.router)

# Episodes management router
app.include_router(episodes.router)
