import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import Addresses, RouteTypes, TransportTypes


@allure.feature("Taxi Order Preparation")
@allure.story("Preparing taxi order before confirmation")
class TestTaxiOrderPreparation:
    """Test class for taxi order preparation functionality.

    Test Scenario 3: Taxi Order Preparation
    Preconditions: Enter two different preset addresses into From and To
    """

    # Route Type Switching Tests
    @allure.title("Verify route type tabs are displayed")
    @allure.description(
        "Check that Optimal, Fast, and Custom route type tabs are displayed"
    )
    def test_route_type_tabs_displayed(self, open_main_page):
        """Test that all route type tabs are visible."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Verify route options block is displayed"):
            assert route_page.is_route_options_displayed(), (
                "Route options block should be displayed"
            )

    @allure.title("Verify switching to Optimal route changes active tab")
    @allure.description(
        "Check that when switching to Optimal route, the active tab changes"
    )
    def test_switch_to_optimal_route(self, open_main_page):
        """Test switching to Optimal route type."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Optimal route"):
            route_page.select_optimal_route()

        with allure.step("Verify Optimal tab is active"):
            assert route_page.is_optimal_tab_active(), (
                "Optimal tab should be active after selection"
            )

    @allure.title("Verify switching to Fast route changes active tab")
    @allure.description(
        "Check that when switching to Fast route, the active tab changes"
    )
    def test_switch_to_fast_route(self, open_main_page):
        """Test switching to Fast route type."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Fast route"):
            route_page.select_fast_route()

        with allure.step("Verify Fast tab is active"):
            assert route_page.is_fast_tab_active(), (
                "Fast tab should be active after selection"
            )

    @allure.title("Verify route time and cost recalculated on route type switch")
    @allure.description(
        "Check that when switching between Optimal and Fast routes, "
        "the time and cost are recalculated"
    )
    def test_route_time_cost_recalculated(self, open_main_page):
        """Test that time and cost change when switching route types."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Optimal route and get values"):
            route_page.select_optimal_route()
            optimal_time = route_page.get_route_travel_time()
            optimal_cost = route_page.get_route_cost()

        with allure.step("Switch to Fast route and get values"):
            route_page.select_fast_route()
            fast_time = route_page.get_route_travel_time()
            fast_cost = route_page.get_route_cost()

        with allure.step("Verify values are recalculated"):
            # At least one value should be different (time or cost)
            values_changed = (optimal_time != fast_time) or (optimal_cost != fast_cost)
            assert values_changed, (
                f"Time or cost should change when switching routes. "
                f"Optimal: time={optimal_time}, cost={optimal_cost}. "
                f"Fast: time={fast_time}, cost={fast_cost}"
            )

    # Custom Route Tests
    @allure.title("Verify switching to Custom route changes active tab")
    @allure.description(
        "Check that when switching to Custom route, the active tab changes"
    )
    def test_switch_to_custom_route(self, open_main_page):
        """Test switching to Custom route type."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Custom route"):
            route_page.select_custom_route()

        with allure.step("Verify Custom tab is active"):
            assert route_page.is_custom_tab_active(), (
                "Custom tab should be active after selection"
            )

    @allure.title("Verify transport types active on Custom route")
    @allure.description(
        "Check that when switching to Custom route, all transport types become active: "
        "Car, Walking, Taxi, Bicycle, Scooter, Drive"
    )
    def test_custom_route_transport_types_active(self, open_main_page):
        """Test that all transport types are available on Custom route."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Custom route"):
            route_page.select_custom_route()

        with allure.step("Verify transport selector is displayed"):
            assert route_page.is_transport_selector_displayed(), (
                "Transport selector should be displayed for Custom route"
            )

        with allure.step("Verify Car transport is visible"):
            assert route_page.is_car_transport_active(), (
                "Car transport should be visible"
            )

        with allure.step("Verify Walking transport is visible"):
            assert route_page.is_walking_transport_visible(), (
                "Walking transport should be visible"
            )

        with allure.step("Verify Taxi transport is visible"):
            assert route_page.is_taxi_transport_visible(), (
                "Taxi transport should be visible"
            )

        with allure.step("Verify Bicycle transport is visible"):
            assert route_page.is_bicycle_transport_visible(), (
                "Bicycle transport should be visible"
            )

        with allure.step("Verify Scooter transport is visible"):
            assert route_page.is_scooter_transport_visible(), (
                "Scooter transport should be visible"
            )

        with allure.step("Verify Drive transport is visible"):
            assert route_page.is_drive_transport_visible(), (
                "Drive transport should be visible"
            )

    # Button State Tests
    @allure.title("Verify Call Taxi button is active on Fast route")
    @allure.description(
        "Check that when Fast route is selected, the Call Taxi button is active"
    )
    def test_call_taxi_button_active_on_fast_route(self, open_main_page):
        """Test that Call Taxi button is enabled on Fast route."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Fast route"):
            route_page.select_fast_route()

        with allure.step("Verify Call Taxi button is displayed"):
            assert route_page.is_call_taxi_button_displayed(), (
                "Call Taxi button should be displayed"
            )

        with allure.step("Verify Call Taxi button is enabled"):
            assert route_page.is_call_taxi_button_enabled(), (
                "Call Taxi button should be enabled when Fast route is selected"
            )

    @allure.title("Verify Book button is active on Custom + Drive")
    @allure.description(
        "Check that when Custom route and Drive transport type are selected, "
        "the Book button is active"
    )
    def test_book_button_active_on_custom_drive(self, open_main_page):
        """Test that Book button is enabled on Custom route with Drive transport."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Custom route"):
            route_page.select_custom_route()

        with allure.step("Select Drive transport type"):
            route_page.select_drive_transport()

        with allure.step("Verify Book button is displayed"):
            assert route_page.is_book_button_displayed(), (
                "Book button should be displayed"
            )

        with allure.step("Verify Book button is enabled"):
            assert route_page.is_book_button_enabled(), (
                "Book button should be enabled when Custom route + Drive is selected"
            )

    @allure.title("Verify switching between route types updates button states")
    @allure.description(
        "Check that button states update correctly when switching between route types"
    )
    def test_button_states_update_on_route_switch(self, open_main_page):
        """Test that buttons update when switching routes."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Build route with different addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Select Fast route and verify Call Taxi button"):
            route_page.select_fast_route()
            assert route_page.is_call_taxi_button_displayed(), (
                "Call Taxi button should be displayed on Fast route"
            )

        with allure.step("Switch to Custom route + Drive and verify Book button"):
            route_page.select_custom_route()
            route_page.select_drive_transport()
            assert route_page.is_book_button_displayed(), (
                "Book button should be displayed on Custom + Drive"
            )
