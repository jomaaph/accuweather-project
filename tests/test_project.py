import json
from unittest.mock import Mock, patch

import pytest

from accuweather_project.create_json_file import create_json_file
from accuweather_project.request import connect_to_accuweather


def test_connect_to_accuweather_returns_api_data():
    response = Mock()
    response.json.return_value = [{"Key": "4651", "LocalizedName": "Luanda"}]

    with patch("accuweather_project.request.requests.get", return_value=response) as get:
        result = connect_to_accuweather(
            "AO",
            "Luanda",
            api_key="test-key",
            url="https://example.test/search",
        )

    get.assert_called_once_with(
        "https://example.test/search",
        params={"apikey": "test-key", "q": "Luanda"},
        timeout=10,
    )
    response.raise_for_status.assert_called_once_with()
    assert result == [{"Key": "4651", "LocalizedName": "Luanda"}]


def test_connect_to_accuweather_requires_api_key(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="API_KEY"):
        connect_to_accuweather("AO", "Luanda", url="https://example.test/search")


def test_connect_to_accuweather_rejects_non_list_response():
    response = Mock()
    response.json.return_value = {"error": "invalid"}

    with patch("accuweather_project.request.requests.get", return_value=response):
        with pytest.raises(ValueError, match="lista"):
            connect_to_accuweather(
                "AO",
                "Luanda",
                api_key="test-key",
                url="https://example.test/search",
            )


def test_connect_to_accuweather_uses_default_for_placeholder_url():
    response = Mock()
    response.json.return_value = []

    with patch("accuweather_project.request.requests.get", return_value=response) as get:
        connect_to_accuweather(
            "AO",
            "Luanda",
            api_key="test-key",
            url="https://example.test/{countryCode}/{adminCode}/search",
        )

    assert get.call_args.args[0] == (
        "https://dataservice.accuweather.com/locations/v1/cities/AO/search"
    )


def test_create_json_file_creates_parent_and_valid_json(tmp_path):
    output_path = tmp_path / "nested" / "result.json"
    data = [{"cidade": "Luanda", "temperatura": 25}]

    result = create_json_file(data, output_path)

    assert result == output_path
    assert json.loads(output_path.read_text(encoding="utf-8")) == data
