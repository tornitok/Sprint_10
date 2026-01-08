import allure
import pytest
from pages.main_page import MainPage
from test_data.addresses import Addresses


@allure.feature("Route Drawing")
@allure.story("Building routes between addresses")
class TestRouteDrawing:
    """Test class for route drawing functionality."""

    @allure.title("Build route with valid preset addresses")
    @allure.description("Verify that a route can be built using the preset addresses")
    def test_build_route_with_valid_addresses(self, open_main_page):
        """Test building a route with valid from and to addresses."""
        main_page = MainPage(open_main_page)

        with allure.step("Enter departure address"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Enter destination address"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Click build route button"):
            main_page.click_build_route()

        with allure.step("Verify route info is displayed"):
            assert main_page.is_route_info_displayed(), "Route info should be displayed after building route"

    @allure.title("Verify map is displayed on main page")
    @allure.description("Check that the map container is visible when the page loads")
    def test_map_is_displayed(self, open_main_page):
        """Test that the map is displayed on the main page."""
        main_page = MainPage(open_main_page)

        with allure.step("Verify map is visible"):
            assert main_page.is_map_displayed(), "Map should be displayed on the main page"

    @allure.title("Verify addresses can be entered in input fields")
    @allure.description("Check that addresses are correctly entered into the input fields")
    def test_address_input_fields_accept_text(self, open_main_page):
        """Test that address input fields accept and retain text."""
        main_page = MainPage(open_main_page)

        with allure.step("Enter from address"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Enter to address"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Verify from address value"):
            from_value = main_page.get_from_input_value()
            assert from_value == Addresses.FROM_ADDRESS, f"Expected '{Addresses.FROM_ADDRESS}', got '{from_value}'"

        with allure.step("Verify to address value"):
            to_value = main_page.get_to_input_value()
            assert to_value == Addresses.TO_ADDRESS, f"Expected '{Addresses.TO_ADDRESS}', got '{to_value}'"

    @allure.title("Build route with reversed addresses")
    @allure.description("Verify that a route can be built with addresses in reverse order")
    def test_build_route_with_reversed_addresses(self, open_main_page):
        """Test building a route with addresses swapped (to becomes from)."""
        main_page = MainPage(open_main_page)

        with allure.step("Enter reversed addresses and build route"):
            main_page.build_route(Addresses.TO_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify route info is displayed"):
            assert main_page.is_route_info_displayed(), "Route info should be displayed for reversed addresses"
