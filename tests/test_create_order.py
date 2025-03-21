import allure
import requests

from conftest import BASE_URL

@allure.story('Test order creation')
class TestCreateOrder:

    @allure.title('Assert status code of successful order creation')
    def test_create_order_authorized(self, auth_token):
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(
            f"{BASE_URL}/orders",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code of create order when unauthorized')
    def test_create_order_unauthorized(self, auth_token):
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(f"{BASE_URL}/orders", json=order_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"

    @allure.title('Assert status code of create order with ingredients')
    def test_create_order_with_ingredients(self, auth_token):
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(
            f"{BASE_URL}/orders",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code of create order without ingredients')
    def test_create_order_without_ingredients(self, auth_token):
        order_data = {"ingredients": []}
        response = requests.post(
            f"{BASE_URL}/orders",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Assert status code of create with wrong ingredient hesh')
    def test_create_order_with_wrong_ingredient_hash(self, auth_token):
        order_data = {"ingredients": ["wrong_ingredient_hash"]}
        response = requests.post(
            f"{BASE_URL}/orders",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 500