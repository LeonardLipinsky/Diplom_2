import allure
import requests

from conftest import BASE_URL

@allure.story('Test user login')
class TestLoginUser:

    @allure.title('Assert status code when try to login with existing user')
    def test_login_existing_user(self, auth_token, user_data):
        response = requests.post(f"{BASE_URL}/auth/login", json=user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code when try to login with incorrect credentials')
    def test_login_incorrect_credentials(self):
        user_data = {
            "email": "nonexistent_user@example.com",
            "password": "wrongpassword",
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"