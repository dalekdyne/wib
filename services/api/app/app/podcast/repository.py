from abc import ABC

from app.podcast.model import Podcast


class Repository(ABC):
    @classmethod
    def create(self, podcast: Podcast):
        raise NotImplementedError(
            "Create method is not implemented on child repository"
        )
