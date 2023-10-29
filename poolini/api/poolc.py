from ..config import config
from .request import get_session

POOLC_API_BASE_URL = config["poolc"]["api"]["base_url"]
POOLC_API_ADMIN_TOKEN = config["poolc"]["api"]["admin_token"]

_session = get_session()
_session.headers = {
    "Authorization": f"Bearer {POOLC_API_ADMIN_TOKEN}",
}


def get_my_activity_hours() -> dict:
    return _session.get(f"{POOLC_API_BASE_URL}").json()


def get_me() -> dict:
    return _session.get(f"{POOLC_API_BASE_URL}/member/me").json()
