import os

import requests
from dotenv import load_dotenv

load_dotenv()


def connect_to_accuweather(location: str) -> list[dict]:
    api_key = os.getenv("API_KEY")
    url = os.getenv("URL")

    if not api_key:
        raise RuntimeError("API_KEY not configured in the environment or in the .env file")
    if not url:
        raise RuntimeError("URL not configured in the environment or in the .env file")

    response = requests.get(
        url,
        params={"apikey": api_key, "q": location},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


