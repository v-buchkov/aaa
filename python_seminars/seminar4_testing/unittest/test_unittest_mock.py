from unittest.mock import patch
import requests


def get_word() -> str:
    result = requests.get("https://example.com/test_case.json").json()
    return result[0]


def test_get_cases():
    with patch("mock_example.requests.get") as mocked_get_cases:
        # Method json -> returns tuple from json
        # Like we used requests, but actually we didn't request
        mocked_get_cases.return_value.json = lambda: ("Hello world!", (10, 2))
        assert get_word() == "Hello world!"
        mocked_get_cases.assert_called_once()
