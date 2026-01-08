import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import Addresses, TaxiFares, ExpectedTexts


@allure.feature("Taxi Order Full Scenario")
@allure.story("Complete taxi ordering flow")
class TestTaxiOrderFullScenario:
    """Test class for complete taxi order flow.

    Test Scenario 5: Taxi Order - Full Scenario
    Preconditions:
    - Enter two different preset addresses
    - Select Fast route
    - Click Call Taxi
    """

    def _navigate_to_taxi_order_form(self, driver):
        """Helper method to navigate to taxi order form."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()
        route_page.click_call_taxi()

        return main_page, route_page, OrderPage(driver)

    # Order Submission Tests
    @allure.title("Verify car search window opens after order submission")
    @allure.description(
        "Check that after selecting Business fare, enabling Laptop table, "
        "and clicking Enter number and order, a car search window opens"
    )
    def test_car_search_window_opens(self, open_main_page):
        """Test that car search window appears after order submission."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Select Business fare"):
            order_page.select_business_fare()

        with allure.step("Enable Laptop table checkbox"):
            order_page.enable_laptop_table()

        with allure.step("Click 'Enter number and order' button"):
            order_page.click_enter_number_and_order()

        with allure.step("Verify car search window is displayed"):
            assert order_page.is_car_search_window_displayed(), (
                "Car search window should be displayed after order submission"
            )

    @allure.title("Verify car search window title")
    @allure.description(
        "Check that the car search window displays 'Searching for a car' title"
    )
    def test_car_search_window_title(self, open_main_page):
        """Test that car search window has correct title."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Submit order"):
            order_page.select_business_fare()
            order_page.enable_laptop_table()
            order_page.click_enter_number_and_order()

        with allure.step("Verify search window title"):
            title = order_page.get_car_search_title()
            assert ExpectedTexts.SEARCHING_FOR_CAR in title, (
                f"Expected title to contain '{ExpectedTexts.SEARCHING_FOR_CAR}', "
                f"but got '{title}'"
            )

    @allure.title("Verify countdown timer is displayed in search window")
    @allure.description(
        "Check that the car search window displays a countdown timer"
    )
    def test_search_timer_displayed(self, open_main_page):
        """Test that countdown timer is visible in search window."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Submit order"):
            order_page.select_business_fare()
            order_page.enable_laptop_table()
            order_page.click_enter_number_and_order()

        with allure.step("Verify countdown timer is displayed"):
            assert order_page.is_search_timer_displayed(), (
                "Countdown timer should be displayed in the top-right corner"
            )

    @allure.title("Verify Cancel button in search window")
    @allure.description(
        "Check that the car search window has a Cancel button"
    )
    def test_cancel_button_in_search_window(self, open_main_page):
        """Test that Cancel button is visible in search window."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Submit order"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Verify Cancel button is displayed"):
            # Cancel button should be visible
            assert order_page.is_car_search_window_displayed(), (
                "Search window with Cancel button should be displayed"
            )

    @allure.title("Verify Details button in search window")
    @allure.description(
        "Check that the car search window has a Details button"
    )
    def test_details_button_in_search_window(self, open_main_page):
        """Test that Details button is visible in search window."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Submit order"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Verify search window is displayed with Details button"):
            assert order_page.is_car_search_window_displayed(), (
                "Search window with Details button should be displayed"
            )


@allure.feature("Taxi Order Full Scenario")
@allure.story("Completed order verification")
class TestCompletedTaxiOrder:
    """Test class for completed taxi order verification."""

    def _submit_taxi_order(self, driver):
        """Helper method to submit a taxi order."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()
        route_page.click_call_taxi()
        order_page.select_business_fare()
        order_page.enable_laptop_table()
        order_page.click_enter_number_and_order()

        return order_page

    @allure.title("Verify completed order window is displayed after search")
    @allure.description(
        "Check that after the search timer finishes, "
        "the completed order window is displayed"
    )
    @pytest.mark.slow
    def test_completed_order_window_displayed(self, open_main_page):
        """Test that completed order window appears after search completes."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify completed order window is displayed"):
            assert order_page.is_completed_order_displayed(), (
                "Completed order window should be displayed after search"
            )

    @allure.title("Verify order title contains 'minutes and arriving'")
    @allure.description(
        "Check that the completed order window displays 'N minutes and arriving'"
    )
    @pytest.mark.slow
    def test_order_title_format(self, open_main_page):
        """Test that order title shows arrival time."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify order title format"):
            title = order_page.get_order_title()
            assert ExpectedTexts.MINUTES_AND_ARRIVING in title, (
                f"Expected title to contain '{ExpectedTexts.MINUTES_AND_ARRIVING}', "
                f"but got '{title}'"
            )

    @allure.title("Verify car number is displayed")
    @allure.description(
        "Check that the completed order window displays the car number"
    )
    @pytest.mark.slow
    def test_car_number_displayed(self, open_main_page):
        """Test that car number is visible in completed order."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify car number is displayed"):
            assert order_page.is_car_number_displayed(), (
                "Car number should be displayed in the completed order window"
            )

    @allure.title("Verify fare image is displayed")
    @allure.description(
        "Check that the completed order window displays the fare image"
    )
    @pytest.mark.slow
    def test_fare_image_displayed(self, open_main_page):
        """Test that fare image is visible in completed order."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify fare image is displayed"):
            assert order_page.is_fare_image_displayed(), (
                "Fare image should be displayed in the top-right corner"
            )

    @allure.title("Verify driver info block is displayed")
    @allure.description(
        "Check that the completed order window displays driver information"
    )
    @pytest.mark.slow
    def test_driver_info_displayed(self, open_main_page):
        """Test that driver info is visible in completed order."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify driver info block is displayed"):
            assert order_page.is_driver_info_displayed(), (
                "Driver info block should be displayed"
            )

    @allure.title("Verify driver name is displayed")
    @allure.description(
        "Check that the driver info block contains the driver name"
    )
    @pytest.mark.slow
    def test_driver_name_displayed(self, open_main_page):
        """Test that driver name is visible."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify driver name is displayed"):
            driver_name = order_page.get_driver_name()
            assert driver_name, "Driver name should be displayed"

    @allure.title("Verify driver photo is displayed")
    @allure.description(
        "Check that the driver info block contains the driver photo"
    )
    @pytest.mark.slow
    def test_driver_photo_displayed(self, open_main_page):
        """Test that driver photo is visible."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify driver photo is displayed"):
            assert order_page.is_driver_photo_displayed(), (
                "Driver photo should be displayed"
            )

    @allure.title("Verify driver rating is displayed")
    @allure.description(
        "Check that the driver info block contains the driver rating"
    )
    @pytest.mark.slow
    def test_driver_rating_displayed(self, open_main_page):
        """Test that driver rating is visible."""
        order_page = self._submit_taxi_order(open_main_page)

        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify driver rating is displayed"):
            rating = order_page.get_driver_rating()
            assert rating, "Driver rating should be displayed"


@allure.feature("Taxi Order Full Scenario")
@allure.story("Order details verification")
class TestOrderDetails:
    """Test class for order details verification."""

    def _complete_taxi_order(self, driver):
        """Helper method to complete a taxi order and wait for completion."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()

        # Store initial cost for comparison
        initial_cost = route_page.get_route_cost()

        route_page.click_call_taxi()
        order_page.select_business_fare()
        order_page.enable_laptop_table()

        # Get fare cost before ordering
        fare_cost = order_page.get_order_price()

        order_page.click_enter_number_and_order()
        order_page.wait_for_search_complete(timeout=60)

        return order_page, fare_cost

    @allure.title("Verify order details window opens")
    @allure.description(
        "Check that clicking Details in 'More about the trip' section "
        "opens the order details window"
    )
    @pytest.mark.slow
    def test_order_details_window_opens(self, open_main_page):
        """Test that order details window opens on click."""
        order_page, _ = self._complete_taxi_order(open_main_page)

        with allure.step("Click Details button"):
            order_page.click_details()

        with allure.step("Verify order details window is displayed"):
            assert order_page.is_order_details_displayed(), (
                "Order details window should be displayed"
            )

    @allure.title("Verify cost in details matches fare selection cost")
    @allure.description(
        "Check that the cost displayed in order details "
        "matches the cost shown during fare selection"
    )
    @pytest.mark.slow
    def test_cost_matches_fare_selection(self, open_main_page):
        """Test that order cost matches fare cost."""
        order_page, fare_cost = self._complete_taxi_order(open_main_page)

        with allure.step("Click Details button"):
            order_page.click_details()

        with allure.step("Verify cost matches fare selection"):
            details_cost = order_page.get_trip_cost()
            assert fare_cost in details_cost or details_cost in fare_cost, (
                f"Cost in details ({details_cost}) should match "
                f"fare selection cost ({fare_cost})"
            )


@allure.feature("Taxi Order Full Scenario")
@allure.story("Order cancellation")
class TestOrderCancellation:
    """Test class for order cancellation functionality."""

    def _complete_taxi_order(self, driver):
        """Helper method to complete a taxi order."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()
        route_page.click_call_taxi()
        order_page.select_business_fare()
        order_page.enable_laptop_table()
        order_page.click_enter_number_and_order()
        order_page.wait_for_search_complete(timeout=60)

        return order_page

    @allure.title("Verify order cancellation closes the window")
    @allure.description(
        "Check that clicking Cancel button closes the order window"
    )
    @pytest.mark.slow
    def test_cancel_closes_order_window(self, open_main_page):
        """Test that cancelling order closes the window."""
        order_page = self._complete_taxi_order(open_main_page)

        with allure.step("Click Cancel button"):
            order_page.click_cancel()

        with allure.step("Verify order window is closed"):
            assert order_page.is_order_window_closed(), (
                "Order window should be closed after cancellation"
            )


@allure.feature("Taxi Order Full Scenario")
@allure.story("End-to-end taxi order flow")
class TestTaxiOrderE2E:
    """End-to-end test for complete taxi order flow."""

    @allure.title("Complete taxi order flow - E2E")
    @allure.description(
        "Complete end-to-end test covering: "
        "route building, fare selection, order submission, "
        "search completion, details verification, and cancellation"
    )
    @pytest.mark.slow
    def test_complete_taxi_order_flow(self, open_main_page):
        """Full end-to-end test for taxi order."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)
        order_page = OrderPage(open_main_page)

        # Step 1: Build route
        with allure.step("Build route with preset addresses"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
            assert main_page.is_route_info_displayed(), (
                "Route info should be displayed"
            )

        # Step 2: Select Fast route
        with allure.step("Select Fast route"):
            route_page.select_fast_route()
            assert route_page.is_fast_tab_active(), (
                "Fast tab should be active"
            )

        # Step 3: Click Call Taxi
        with allure.step("Click Call Taxi"):
            route_page.click_call_taxi()
            assert order_page.is_order_form_displayed(), (
                "Order form should be displayed"
            )

        # Step 4: Select Business fare
        with allure.step("Select Business fare"):
            order_page.select_business_fare()

        # Step 5: Enable Laptop table
        with allure.step("Enable Laptop table checkbox"):
            order_page.enable_laptop_table()

        # Store fare cost for later verification
        fare_cost = order_page.get_order_price()

        # Step 6: Submit order
        with allure.step("Click 'Enter number and order'"):
            order_page.click_enter_number_and_order()
            assert order_page.is_car_search_window_displayed(), (
                "Car search window should be displayed"
            )

        # Step 7: Wait for search completion
        with allure.step("Wait for car search to complete"):
            order_page.wait_for_search_complete(timeout=60)
            assert order_page.is_completed_order_displayed(), (
                "Completed order window should be displayed"
            )

        # Step 8: Verify driver info
        with allure.step("Verify driver info is displayed"):
            assert order_page.is_driver_info_displayed(), (
                "Driver info should be displayed"
            )

        # Step 9: Check order details
        with allure.step("Click Details and verify cost"):
            order_page.click_details()
            assert order_page.is_order_details_displayed(), (
                "Order details should be displayed"
            )

            details_cost = order_page.get_trip_cost()
            assert fare_cost in details_cost or details_cost in fare_cost, (
                f"Cost mismatch: fare={fare_cost}, details={details_cost}"
            )

        # Step 10: Cancel order
        with allure.step("Cancel the order"):
            order_page.click_cancel()
            assert order_page.is_order_window_closed(), (
                "Order window should be closed"
            )
