import allure
import requests

from conftest import BASE_URL, ERROR_401, AUTH_USER


@allure.story('Test user update')
class TestUserUpdate:

    @allure.title('Assert status code when try to update with authorized user')
    def test_update_user_authorized(self, auth_token, update_user_data):

        response = requests.patch(
            f"{BASE_URL}{AUTH_USER}",
            headers={"Authorization": auth_token[0]},
            json=update_user_data,
        )
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Updated User"

    @allure.title('Assert status code when try to update with unauthorized user')
    def test_update_user_unauthorized(self, update_user_data):
        response = requests.patch(f"{BASE_URL}{AUTH_USER}", json=update_user_data)
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_401