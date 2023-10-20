import datetime
import unittest
import uuid

from app.episode.model import PodcastEpisode
from infra.mongodb.episode.repository import EpisodeRepository


class RepositoryTestCases(unittest.TestCase):
    def test_create_episode(self):
        pe = PodcastEpisode(
            title="Title",
            description="Description",
            streams=0,
            release_date=datetime.datetime.now(),
            type="Podcast",
            rating="",
            artwork="",
            audio="",
            status="Scheduled",
            podcast_id="123456789",
            user_id=uuid.uuid4(),
        )

        repository = EpisodeRepository()

        w = repository.create(pe)

        self.assertIsNotNone(w)

    def test_update_episode(self):
        pe = PodcastEpisode(
            title="One title",
            description="One Description",
            streams=0,
            release_date=datetime.datetime.now(),
            type="Podcast",
            rating="",
            artwork="",
            audio="",
            status="Scheduled",
            podcast_id="123456789",
            user_id=uuid.uuid4(),
        )

        repository = EpisodeRepository()

        id = repository.create(pe)

        pe.title = "Updated Title"
        pe.status = "Published"

        w = repository.update(id, pe)

        self.assertIsNotNone(w)

    def test_delete_episode(self):
        pe = PodcastEpisode(
            title="One title",
            description="One Description",
            streams=0,
            release_date=datetime.datetime.now(),
            type="Podcast for deletion",
            rating="",
            artwork="",
            audio="",
            status="Scheduled",
            podcast_id="123456789",
            user_id=uuid.uuid4(),
        )

        repository = EpisodeRepository()

        id = repository.create(pe)
        self.assertIsNotNone(id)

        deletedID = repository.deleteById(id)
        self.assertIsNotNone(deletedID)

        podcastEpisode = repository.getById(deletedID)
        self.assertIsNone(podcastEpisode)

    def test_get_episode(self):
        pe = PodcastEpisode(
            title="One title",
            description="One Description",
            streams=0,
            release_date=datetime.datetime.now(),
            type="Podcast for fetching",
            rating="",
            artwork="",
            audio="",
            status="Scheduled",
            podcast_id="123456789",
            user_id=uuid.uuid4(),
        )

        repository = EpisodeRepository()

        id = repository.create(pe)
        self.assertIsNotNone(id)

        podcastEpisode = repository.getById(id)
        self.assertIsNotNone(podcastEpisode)
        self.assertEqual(podcastEpisode["title"], pe.title)


if __name__ == "__main__":
    unittest.main()
