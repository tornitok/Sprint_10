import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from test_data.addresses import Addresses, ExpectedTexts


@allure.feature("Route Options")
@allure.story("Route options block functionality")
class TestRouteOptionsBlock:
    """Test class for route options block functionality.

    Test Scenario 2: Route Options Block Rendering
    """

    @allure.title("Scenario A: Verify route options displayed with different addresses")
    @allure.description(
        "Check that route options block appears under the address input fields "
        "when two different preset addresses are entered"
    )
    def test_route_options_displayed_with_different_addresses(self, open_main_page):
        """Test that route options are displayed after building a route with different addresses."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with two different preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify route options block is displayed"):
            assert route_page.is_route_options_displayed(), (
                "Route options block should be displayed under address input fields"
            )

    @allure.title("Scenario B: Verify route options displayed with same addresses")
    @allure.description(
        "Check that route options block is displayed when the same preset address "
        "is entered in both From and To fields"
    )
    def test_route_options_displayed_with_same_addresses(self, open_main_page):
        """Test that route options are displayed when same address is used."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with the same preset address in both fields"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify route options block is displayed"):
            assert route_page.is_route_options_displayed(), (
                "Route options block should be displayed even with same addresses"
            )

    @allure.title("Scenario B: Verify same address route shows Auto type")
    @allure.description(
        "Check that when same address is used, the route type displays 'Auto'"
    )
    def test_same_address_shows_auto_route_type(self, open_main_page):
        """Test that same address route shows Auto as route type."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with the same preset address"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify route type shows 'Auto'"):
            route_type = route_page.get_route_type_text()
            assert ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE in route_type, (
                f"Expected route type to contain '{ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE}', "
                f"but got '{route_type}'"
            )

    @allure.title("Scenario B: Verify same address route shows Free cost")
    @allure.description(
        "Check that when same address is used, the cost displays 'Free'"
    )
    def test_same_address_shows_free_cost(self, open_main_page):
        """Test that same address route shows Free as cost."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with the same preset address"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify cost shows 'Free'"):
            cost = route_page.get_cost_text()
            assert ExpectedTexts.SAME_ADDRESS_COST in cost, (
                f"Expected cost to contain '{ExpectedTexts.SAME_ADDRESS_COST}', "
                f"but got '{cost}'"
            )

    @allure.title("Scenario B: Verify same address route shows zero travel time")
    @allure.description(
        "Check that when same address is used, the travel time displays '0 min'"
    )
    def test_same_address_shows_zero_travel_time(self, open_main_page):
        """Test that same address route shows 0 min travel time."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with the same preset address"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify travel time shows '0 min'"):
            travel_time = route_page.get_route_travel_time()
            assert ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME in travel_time, (
                f"Expected travel time to contain '{ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME}', "
                f"but got '{travel_time}'"
            )

    @allure.title("Scenario B: Verify same address complete block content")
    @allure.description(
        "Check that when same address is used, all expected text is displayed: "
        "Auto, Free, Travel time: 0 min"
    )
    def test_same_address_complete_block_content(self, open_main_page):
        """Test complete content verification for same address route."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build a route with the same preset address"):
            main_page.build_route(Addresses.TO_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify route options block is displayed"):
            assert route_page.is_route_options_displayed(), (
                "Route options block should be displayed"
            )

        with allure.step("Verify all expected texts are present"):
            route_type = route_page.get_route_type_text()
            cost = route_page.get_cost_text()
            travel_time = route_page.get_route_travel_time()

            errors = []
            if ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE not in route_type:
                errors.append(
                    f"Route type: expected '{ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE}', "
                    f"got '{route_type}'"
                )
            if ExpectedTexts.SAME_ADDRESS_COST not in cost:
                errors.append(
                    f"Cost: expected '{ExpectedTexts.SAME_ADDRESS_COST}', got '{cost}'"
                )
            if ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME not in travel_time:
                errors.append(
                    f"Travel time: expected '{ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME}', "
                    f"got '{travel_time}'"
                )

            assert not errors, "\n".join(errors)
