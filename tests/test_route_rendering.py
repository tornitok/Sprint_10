import allure
import pytest
from pages.main_page import MainPage
from test_data.addresses import Addresses


@allure.feature("Route Rendering")
@allure.story("Route visualization on map")
class TestRouteRendering:
    """Test class for route rendering functionality.

    Test Scenario 1: Route Rendering
    Preconditions: Enter two different preset addresses into From and To fields
    """

    @allure.title("Verify route is rendered on the map")
    @allure.description(
        "Check that after entering two different preset addresses, "
        "the route is rendered on the map"
    )
    def test_route_rendered_on_map(self, open_main_page):
        """Test that route is rendered after entering valid addresses."""
        main_page = MainPage(open_main_page)

        with allure.step("Build route with two different preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify route line is displayed on the map"):
            assert main_page.is_route_line_displayed(), (
                "Route line should be rendered on the map after building route"
            )

    @allure.title("Verify start point marker is displayed on map")
    @allure.description(
        "Check that the map displays a start point marker "
        "after building a route"
    )
    def test_start_marker_displayed(self, open_main_page):
        """Test that start point marker appears on the map."""
        main_page = MainPage(open_main_page)

        with allure.step("Build route with two different preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify start point marker is displayed"):
            assert main_page.is_start_marker_displayed(), (
                "Start point marker should be visible on the map"
            )

    @allure.title("Verify end point marker is displayed on map")
    @allure.description(
        "Check that the map displays an end point marker "
        "after building a route"
    )
    def test_end_marker_displayed(self, open_main_page):
        """Test that end point marker appears on the map."""
        main_page = MainPage(open_main_page)

        with allure.step("Build route with two different preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify end point marker is displayed"):
            assert main_page.is_end_marker_displayed(), (
                "End point marker should be visible on the map"
            )

    @allure.title("Verify both markers are displayed simultaneously")
    @allure.description(
        "Check that both start and end markers are displayed on the map "
        "at the same time after building a route"
    )
    def test_both_markers_displayed(self, open_main_page):
        """Test that both start and end markers appear together."""
        main_page = MainPage(open_main_page)

        with allure.step("Build route with two different preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify both markers are displayed"):
            start_visible = main_page.is_start_marker_displayed()
            end_visible = main_page.is_end_marker_displayed()

            assert start_visible and end_visible, (
                f"Both markers should be visible. "
                f"Start marker: {start_visible}, End marker: {end_visible}"
            )

    @allure.title("Verify route rendering with reversed addresses")
    @allure.description(
        "Check that route is rendered correctly when addresses are "
        "entered in reverse order (To address in From field and vice versa)"
    )
    def test_route_rendered_with_reversed_addresses(self, open_main_page):
        """Test route rendering with addresses swapped."""
        main_page = MainPage(open_main_page)

        with allure.step("Build route with reversed addresses"):
            main_page.build_route(Addresses.TO_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Verify route line is displayed"):
            assert main_page.is_route_line_displayed(), (
                "Route should be rendered with reversed addresses"
            )

        with allure.step("Verify both markers are displayed"):
            assert main_page.is_start_marker_displayed(), (
                "Start marker should be visible with reversed addresses"
            )
            assert main_page.is_end_marker_displayed(), (
                "End marker should be visible with reversed addresses"
            )
