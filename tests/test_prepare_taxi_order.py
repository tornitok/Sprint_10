import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data.addresses import Addresses


@allure.feature("Taxi Order Preparation")
@allure.story("Preparing taxi order before confirmation")
class TestPrepareTaxiOrder:
    """Test class for taxi order preparation functionality."""

    @allure.title("Verify order taxi button appears after building route")
    @allure.description("Check that the order taxi button is visible after route is built")
    def test_order_taxi_button_displayed_after_route(self, open_main_page):
        """Test that order taxi button appears after building a route."""
        main_page = MainPage(open_main_page)

        with allure.step("Build a route"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify order taxi button is displayed"):
            assert main_page.is_order_taxi_button_displayed(), "Order taxi button should be displayed"
