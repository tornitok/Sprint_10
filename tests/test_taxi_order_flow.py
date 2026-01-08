import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data.addresses import Addresses


@allure.feature("Taxi Order Flow")
@allure.story("Complete taxi ordering process")
class TestTaxiOrderFlow:
    """Test class for complete taxi order flow."""

    @allure.title("Navigate to order form after building route")
    @allure.description("Verify user can navigate to order form from built route")
    def test_navigate_to_order_form(self, open_main_page):
        """Test navigation from route to order form."""
        main_page = MainPage(open_main_page)
        order_page = OrderPage(open_main_page)

        with allure.step("Build a route"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Click order taxi button"):
            main_page.click_order_taxi()

        with allure.step("Verify order form is displayed"):
            assert order_page.is_order_form_displayed(), "Order form should be displayed"
