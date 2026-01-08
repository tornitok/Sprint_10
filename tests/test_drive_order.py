import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import (
    Addresses,
    DriveFares,
    DriveFareDescriptions,
    ExpectedTexts,
)


@allure.feature("Drive Order")
@allure.story("Drive order functionality")
class TestDriveOrder:
    """Test class for Drive order functionality.

    Drive Order Block - Technical Specification
    Preconditions:
    - Enter two different preset addresses
    - Select Custom route
    - Select Drive transport type
    - Click Book button
    """

    def _navigate_to_drive_order(self, driver):
        """Helper method to navigate to Drive order form."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        return main_page, route_page, OrderPage(driver)

    # Drive Fares Tests
    @allure.title("Verify Drive order form opens after Book")
    @allure.description(
        "Check that clicking Book button opens the Drive order form"
    )
    def test_drive_order_form_opens(self, open_main_page):
        """Test that Drive order form is displayed."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Verify Drive order form is displayed"):
            assert order_page.is_drive_order_form_displayed(), (
                "Drive order form should be displayed after clicking Book"
            )

    @allure.title("Verify Everyday fare is available")
    @allure.description("Check that Everyday Drive fare is displayed")
    def test_everyday_fare_available(self, open_main_page):
        """Test Everyday fare visibility."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Verify Everyday fare is visible"):
            assert order_page.is_fare_visible("everyday"), (
                "Everyday fare should be visible"
            )

    @allure.title("Verify Outdoor fare is available")
    @allure.description("Check that Outdoor Drive fare is displayed")
    def test_outdoor_fare_available(self, open_main_page):
        """Test Outdoor fare visibility."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Verify Outdoor fare is visible"):
            assert order_page.is_fare_visible("outdoor"), (
                "Outdoor fare should be visible"
            )

    @allure.title("Verify Luxury fare is available")
    @allure.description("Check that Luxury Drive fare is displayed")
    def test_luxury_fare_available(self, open_main_page):
        """Test Luxury fare visibility."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Verify Luxury fare is visible"):
            assert order_page.is_fare_visible("luxury"), (
                "Luxury fare should be visible"
            )

    @allure.title("Verify all Drive fares are present")
    @allure.description(
        "Check that all Drive fares are displayed: Everyday, Outdoor, Luxury"
    )
    def test_all_drive_fares_present(self, open_main_page):
        """Test that all Drive fares are available."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Verify all Drive fares are visible"):
            missing_fares = []
            for fare in DriveFares.ALL_FARES:
                if not order_page.is_fare_visible(fare.lower()):
                    missing_fares.append(fare)

            assert not missing_fares, (
                f"Missing Drive fares: {missing_fares}. "
                f"Expected all of: {DriveFares.ALL_FARES}"
            )


@allure.feature("Drive Order")
@allure.story("Drive fare descriptions")
class TestDriveFareDescriptions:
    """Test class for Drive fare description tooltips."""

    def _navigate_to_drive_order(self, driver):
        """Helper method to navigate to Drive order form."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        return OrderPage(driver)

    @allure.title("Verify Everyday fare description")
    @allure.description(
        "Check that Everyday fare tooltip shows 'BMW 750, simple daily trips'"
    )
    def test_everyday_fare_description(self, open_main_page):
        """Test Everyday fare tooltip description."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Hover over Everyday fare info icon"):
            order_page.hover_fare_info_icon("everyday")

        with allure.step("Verify tooltip text"):
            tooltip_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.EVERYDAY
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Outdoor fare description")
    @allure.description(
        "Check that Outdoor fare tooltip shows 'KIA RIO, for traveling'"
    )
    def test_outdoor_fare_description(self, open_main_page):
        """Test Outdoor fare tooltip description."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Hover over Outdoor fare info icon"):
            order_page.hover_fare_info_icon("outdoor")

        with allure.step("Verify tooltip text"):
            tooltip_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.OUTDOOR
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Luxury fare description")
    @allure.description(
        "Check that Luxury fare tooltip shows 'PORSCHE 911, shine and power'"
    )
    def test_luxury_fare_description(self, open_main_page):
        """Test Luxury fare tooltip description."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Hover over Luxury fare info icon"):
            order_page.hover_fare_info_icon("luxury")

        with allure.step("Verify tooltip text"):
            tooltip_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.LUXURY
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )


@allure.feature("Drive Order")
@allure.story("Add Driver License Window")
class TestAddDriverLicenseWindow:
    """Test class for Add Driver License window functionality."""

    def _navigate_to_license_window(self, driver):
        """Helper method to navigate to driver license window."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()
        order_page.select_everyday_fare()
        # Assuming there's a button to trigger license window
        order_page.click_enter_number_and_order()

        return order_page

    @allure.title("Verify license window is displayed")
    @allure.description(
        "Check that the Add Driver License window is displayed when needed"
    )
    def test_license_window_displayed(self, open_main_page):
        """Test that license window appears."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify license window is displayed"):
            assert order_page.is_license_window_displayed(), (
                "Add Driver License window should be displayed"
            )

    @allure.title("Verify first name field is present")
    @allure.description(
        "Check that the license form contains a First name field"
    )
    def test_first_name_field_present(self, open_main_page):
        """Test first name field is visible."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify first name field is displayed"):
            assert order_page.is_first_name_field_displayed(), (
                "First name field should be present"
            )

    @allure.title("Verify last name field is present")
    @allure.description(
        "Check that the license form contains a Last name field"
    )
    def test_last_name_field_present(self, open_main_page):
        """Test last name field is visible."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify last name field is displayed"):
            assert order_page.is_last_name_field_displayed(), (
                "Last name field should be present"
            )

    @allure.title("Verify date of birth field is present")
    @allure.description(
        "Check that the license form contains a Date of birth field"
    )
    def test_date_of_birth_field_present(self, open_main_page):
        """Test date of birth field is visible."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify date of birth field is displayed"):
            assert order_page.is_date_of_birth_field_displayed(), (
                "Date of birth field should be present"
            )

    @allure.title("Verify license number field is present")
    @allure.description(
        "Check that the license form contains a License number field"
    )
    def test_license_number_field_present(self, open_main_page):
        """Test license number field is visible."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify license number field is displayed"):
            assert order_page.is_license_number_field_displayed(), (
                "License number field should be present"
            )

    @allure.title("Verify all license form fields are present")
    @allure.description(
        "Check that all required fields are present: "
        "First name, Last name, Date of birth, License number"
    )
    def test_all_license_fields_present(self, open_main_page):
        """Test all license form fields are visible."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Verify all license fields"):
            missing_fields = []

            if not order_page.is_first_name_field_displayed():
                missing_fields.append("First name")

            if not order_page.is_last_name_field_displayed():
                missing_fields.append("Last name")

            if not order_page.is_date_of_birth_field_displayed():
                missing_fields.append("Date of birth")

            if not order_page.is_license_number_field_displayed():
                missing_fields.append("License number")

            assert not missing_fields, (
                f"Missing license fields: {missing_fields}"
            )


@allure.feature("Drive Order")
@allure.story("Completed Drive Order Window")
class TestCompletedDriveOrder:
    """Test class for Completed Drive Order window."""

    def _complete_drive_order(self, driver):
        """Helper method to complete a Drive order."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()
        order_page.select_everyday_fare()
        order_page.click_enter_number_and_order()

        # Fill license if required
        if order_page.is_license_window_displayed():
            order_page.enter_first_name("John")
            order_page.enter_last_name("Doe")
            order_page.enter_date_of_birth("01/01/1990")
            order_page.enter_license_number("ABC123456")
            order_page.click_add_license()

        return order_page

    @allure.title("Verify completed Drive order window title")
    @allure.description(
        "Check that the completed Drive order window shows 'Car booked' title"
    )
    @pytest.mark.slow
    def test_drive_order_title(self, open_main_page):
        """Test completed Drive order window title."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify Drive order window is displayed"):
            assert order_page.is_drive_order_window_displayed(), (
                "Completed Drive order window should be displayed"
            )

    @allure.title("Verify free waiting timer is displayed")
    @allure.description(
        "Check that the completed Drive order shows free waiting timer"
    )
    @pytest.mark.slow
    def test_free_waiting_timer_displayed(self, open_main_page):
        """Test free waiting timer visibility."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify free waiting timer is displayed"):
            assert order_page.is_free_waiting_timer_displayed(), (
                "Free waiting timer should be displayed in top-right corner"
            )

    @allure.title("Verify fare image and name are displayed")
    @allure.description(
        "Check that the completed Drive order shows fare image and name"
    )
    @pytest.mark.slow
    def test_fare_image_displayed(self, open_main_page):
        """Test fare image visibility."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify fare image is displayed"):
            assert order_page.is_fare_image_displayed(), (
                "Fare image and name should be displayed"
            )

    @allure.title("Verify car location address is displayed")
    @allure.description(
        "Check that the completed Drive order shows car location address"
    )
    @pytest.mark.slow
    def test_car_location_displayed(self, open_main_page):
        """Test car location address visibility."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Verify car location address is displayed"):
            location = order_page.get_car_location_address()
            assert location, (
                "Car location address (From) should be displayed"
            )

    @allure.title("Verify trip cost is displayed in More about the trip")
    @allure.description(
        "Check that the completed Drive order shows cost in More about the trip"
    )
    @pytest.mark.slow
    def test_trip_cost_displayed(self, open_main_page):
        """Test trip cost visibility."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Click Details"):
            order_page.click_details()

        with allure.step("Verify trip cost is displayed"):
            cost = order_page.get_trip_cost()
            assert cost, (
                "Trip cost should be displayed in More about the trip section"
            )

    @allure.title("Verify Cancel button closes Drive order window")
    @allure.description(
        "Check that clicking Cancel closes the Drive order window"
    )
    @pytest.mark.slow
    def test_cancel_closes_drive_order(self, open_main_page):
        """Test Drive order cancellation."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Wait for Drive order to complete"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Click Cancel button"):
            order_page.click_cancel()

        with allure.step("Verify order window is closed"):
            assert order_page.is_order_window_closed(), (
                "Drive order window should be closed after cancellation"
            )
