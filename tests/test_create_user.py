import allure
import requests
from conftest import BASE_URL

@allure.story('Test user creation')
class TestCreateUser:

    @allure.title('Assert status code of successful user creation')
    def test_create_unique_user(self, user_data):
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        access_token = response.json()["accessToken"]
        assert response.status_code == 200
        assert response.json()["success"] is True
        requests.delete(
            f"{BASE_URL}/auth/user", headers={"Authorization": access_token}
        )

    @allure.title('Assert status code of when trying to create already registered user')
    def test_create_already_registered_user(self, user_data):
        first_register_response = requests.post(
            f"{BASE_URL}/auth/register", json=user_data
        )
        assert first_register_response.status_code == 200
        access_token = first_register_response.json()["accessToken"]
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"
        requests.delete(
            f"{BASE_URL}/auth/user", headers={"Authorization": access_token}
        )

    @allure.title('Assert status code when creating user with missing required filed ')
    def test_create_user_with_missing_required_field(self, auth_token, user_data):
        incomplete_user_data = user_data.copy()
        incomplete_user_data.pop("email")
        response = requests.post(f"{BASE_URL}/auth/register", json=incomplete_user_data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert (
            response.json()["message"] == "Email, password and name are required fields"
        )