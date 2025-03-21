import pytest
import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


@pytest.fixture(scope="module")
def user_data():
    return {
        "email": "unique_test_user@example.com",
        "password": "password12345",
        "name": "Unique User",
    }


@pytest.fixture(scope="module")
def auth_token(user_data):
    # register user, return token and after delete user
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    auth_token = response.json()["accessToken"]
    refresh_token = response.json()["refreshToken"]
    yield auth_token, refresh_token
    requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": auth_token})
