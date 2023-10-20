from datetime import datetime
import hashlib
import json
from bson import json_util
import requests
import uuid
from urllib.parse import urlparse
import os
from fastapi.logger import logger


def parse_json(data):
    return json.loads(json_util.dumps(data))


def fetch_remote_file(url):
    try:
        data = requests.get(url).content
        return data
    except Exception as e:
        logger.error("Couldn't fetch remote file: " + str(e))
        return False


def generate_short_id():
    uid = uuid.uuid4()
    return str(uid)[:8]


def get_file_extension(url):
    try:
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]
        return ext
    except Exception as e:
        logger.error("Couldn't get file extension: " + str(e))
        return False


# UTC dates
def is_date_in_future(date):
    return date > datetime.utcnow()


# Load file contents from html file to string
def load_file_contents(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        logger.error("Couldn't load file contents: " + str(e))
        return False


def str_to_sha1(str):
    return hashlib.sha1(str.encode()).hexdigest()


def str_to_md5(str):
    return hashlib.md5(str.encode()).hexdigest()
