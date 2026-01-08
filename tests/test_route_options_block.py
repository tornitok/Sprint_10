import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from test_data.addresses import Addresses


@allure.feature("Route Options")
@allure.story("Route options block functionality")
class TestRouteOptionsBlock:
    """Test class for route options block functionality."""

    @allure.title("Verify route options are displayed after building route")
    @allure.description("Check that route options block appears after a route is built")
    def test_route_options_displayed_after_route_built(self, open_main_page):
        """Test that route options are displayed after building a route."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify route options block is displayed"):
            assert route_page.is_route_options_displayed(), "Route options should be displayed"
