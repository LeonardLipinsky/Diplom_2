import allure
import requests

from conftest import BASE_URL, ERROR_401, ORDERS_URL


@allure.story('Test get orders')
class TestGetOrders:

    @allure.title('Assert status code when user get orders while being authorized')
    def test_get_orders_authorized(self, auth_token, order_data):
        response = requests.post(
            f"{BASE_URL}{ORDERS_URL}",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        assert response.status_code == 200
        response = requests.get(
            f"{BASE_URL}{ORDERS_URL}", headers={"Authorization": auth_token[0]}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code when user get orders while being unauthorized')
    def test_get_orders_unauthorized(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}")
        assert response.status_code == 401
        assert response.json()["message"] == ERROR_401