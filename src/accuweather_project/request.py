from __future__ import annotations

import os
from typing import Any

import requests
from dotenv import load_dotenv

DEFAULT_URL = "https://dataservice.accuweather.com/locations/v1/cities/{country_code}/search"

load_dotenv()


def connect_to_accuweather(
    country_code: str,
    location: str,
    *,
    api_key: str | None = None,
    url: str | None = None,
    timeout: float = 10,
) -> list[dict[str, Any]]:
    """Search for cities in AccuWeather by country code and location."""
    resolved_api_key = api_key or os.getenv("API_KEY")
    if not resolved_api_key:
        raise RuntimeError("API_KEY nao configurada no ambiente ou no arquivo .env")

    endpoint = url or os.getenv("URL") or DEFAULT_URL.format(country_code=country_code)
    if "{" in endpoint or "}" in endpoint:
        endpoint = DEFAULT_URL.format(country_code=country_code)
    response = requests.get(
        endpoint,
        params={"apikey": resolved_api_key, "q": location},
        timeout=timeout,
    )
    response.raise_for_status()

    data = response.json()
    if not isinstance(data, list):
        raise ValueError("A resposta da API deve ser uma lista de localidades")
    return data


