import requests
from requests.sessions import Session
from requests.adapters import HTTPAdapter, Retry

CONNECTION_TIMEOUT_S = 1
READ_TIMEOUT_S = 5
BACKOFF_FACTOR_S = 0.5


def get_session() -> Session:
    s = requests.Session()

    retry = Retry(
        connect=CONNECTION_TIMEOUT_S,
        read=READ_TIMEOUT_S,
        backoff_factor=BACKOFF_FACTOR_S,
    )

    adapter = HTTPAdapter(max_retries=retry)
    s.mount("http://", adapter)
    s.mount("https://", adapter)

    return s
