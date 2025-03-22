import pytest
import requests
import helpers

BASE_URL = "https://stellarburgers.nomoreparties.site/api"
ORDERS_URL = "/orders"
AUTH_LOGIN = "/auth/login"
AUTH_USER = "/auth/user"
AUTH_REGISTER = "/auth/register"


ERROR_401 = "You should be authorised"
ERROR_400 = "Ingredient ids must be provided"
ERROR_403 = "Email, password and name are required fields"
ERROR_403_user = "User already exists"
ERROR_401_email = "email or password are incorrect"



@pytest.fixture(scope="module")
def user_data():
    return {
        "email": helpers.create_random_email(),
        "password": helpers.create_random_password(),
        "name": helpers.create_random_name(),
    }

@pytest.fixture
def ingredients():
    return [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6f"
    ]

@pytest.fixture
def order_data(ingredients):
    return {
        "ingredients": ingredients
    }

@pytest.fixture
def update_user_data():
    return {"name": "Updated User"}

@pytest.fixture
def order_data_wrong_ingredient():
    return {"ingredients": ["wrong_ingredient_hash"]}


@pytest.fixture
def wrong_user_data():
    return {
            "email": "nonexistent_user@example.com",
            "password": "wrongpassword",
        }

@pytest.fixture
def order_data_none():
    return {"ingredients": []}

@pytest.fixture(scope="module")
def auth_token(user_data):
    # register user, return token and after delete user
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    auth_token = response.json()["accessToken"]
    refresh_token = response.json()["refreshToken"]
    yield auth_token, refresh_token
    requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": auth_token})
