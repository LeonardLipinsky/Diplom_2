import allure
import requests

from conftest import BASE_URL

@allure.story('Test get orders')
class TestGetOrders:

    @allure.title('Assert status code when user get orders while being authorized')
    def test_get_orders_authorized(self, auth_token):
        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(
            f"{BASE_URL}/orders",
            headers={"Authorization": auth_token[0]},
            json=order_data,
        )
        response = requests.get(
            f"{BASE_URL}/orders", headers={"Authorization": auth_token[0]}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Assert status code when user get orders while being unauthorized')
    def test_get_orders_unauthorized(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"