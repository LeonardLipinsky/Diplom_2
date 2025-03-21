import allure
import requests

from conftest import BASE_URL

@allure.story('Test user update')
class TestUserUpdate:

    @allure.title('Assert status code when try to update with authorized user')
    def test_update_user_authorized(self, auth_token):
        update_data = {"name": "Updated User"}
        response = requests.patch(
            f"{BASE_URL}/auth/user",
            headers={"Authorization": auth_token[0]},
            json=update_data,
        )
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Updated User"

    @allure.title('Assert status code when try to update with unauthorized user')
    def test_update_user_unauthorized(self):
        update_data = {"name": "Updated User"}
        response = requests.patch(f"{BASE_URL}/auth/user", json=update_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"