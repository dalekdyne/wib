import requests
import time

from core.helpers import str_to_md5, str_to_sha1
from config import ConfigParams


class PodcastIndex:
    URL = "https://api.podcastindex.org/api/1.0/"

    def __init__(self):
        pass

    def submit_podcast(self, podcast):
        """
        Submit podcast to PodcastIndex
        podcast: dict
        """
        endpoint = "add/byfeedurl"

        podcast_chash = str_to_md5(
            podcast["title"]
            + podcast["website"]
            + podcast["language"]
            + "podhustlr"  # Feed generator
            + podcast["creator"]
            + podcast["creator"]
            + podcast["email"]
        )

        params = {"url": podcast["feed_url"], "chash": podcast_chash}

        now = int(time.time())
        headers = {
            "User-Agent": "podhustlr-api",
            "X-Auth-Key": ConfigParams.PODCASTINDEX_API_KEY,
            "X-Auth-Date": str(now),
            "Authorization": str_to_sha1(
                ConfigParams.PODCASTINDEX_API_KEY
                + ConfigParams.PODCASTINDEX_API_SECRET
                + str(now)
            ),
        }

        response = requests.get(
            PodcastIndex.URL + endpoint, params=params, headers=headers
        )

        if response.status_code == 200 or response.status_code == 302:
            return True
        else:
            return False
