import allure
import requests

from conftest import BASE_URL, ERROR_401, ERROR_400, ORDERS_URL


@allure.story('Test order creation')
class TestCreateOrder:

    @allure.title('Assert status code of successful order creation')
    def test_create_order_authorized(self, auth_token, order_data):
        response = requests.post(
            f"{BASE_URL}{ORDERS_URL}",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code of create order when unauthorized')
    def test_create_order_unauthorized(self, auth_token, order_data):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=order_data)
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_401

    @allure.title('Assert status code of create order with ingredients')
    def test_create_order_with_ingredients(self, auth_token, order_data):
        response = requests.post(
            f"{BASE_URL}{ORDERS_URL}",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code of create order without ingredients')
    def test_create_order_without_ingredients(self, auth_token, order_data_none):
        response = requests.post(
            f"{BASE_URL}{ORDERS_URL}",
            headers={"Authorization": auth_token[0]},
            json=order_data_none,
        )
        assert response.status_code == 400
        assert response.json()["message"] == ERROR_400

    @allure.title('Assert status code of create with wrong ingredient hesh')
    def test_create_order_with_wrong_ingredient_hash(self, auth_token,order_data_wrong_ingredient):
        response = requests.post(
            f"{BASE_URL}{ORDERS_URL}",
            headers={"Authorization": auth_token[0]},
            json=order_data_wrong_ingredient,
        )
        assert response.status_code == 500