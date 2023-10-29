import requests
from requests.sessions import Session
from requests.adapters import HTTPAdapter, Retry

from ..config import config

POOLC_API_BASE_URL = config["poolc"]["api"]["base_url"]
POOLC_API_ADMIN_TOKEN = config["poolc"]["api"]["admin_token"]
CONNECTION_TIMEOUT_S = 1
READ_TIMEOUT_S = 5
BACKOFF_FACTOR_S = 0.5


def get_my_activity_hours() -> dict:
    return _request().get(f"{POOLC_API_BASE_URL}").json()


def get_me() -> dict:
    return _request().get(f"{POOLC_API_BASE_URL}/member/me").json()


def _request() -> Session:
    s = requests.Session()

    retry = Retry(
        connect=CONNECTION_TIMEOUT_S,
        read=READ_TIMEOUT_S,
        backoff_factor=BACKOFF_FACTOR_S,
    )

    adapter = HTTPAdapter(max_retries=retry)
    s.mount("http://", adapter)
    s.mount("https://", adapter)

    s.headers = {
        "Authorization": f"Bearer {POOLC_API_ADMIN_TOKEN}",
    }

    return s
