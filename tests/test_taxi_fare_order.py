import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import (
    Addresses,
    TaxiFares,
    TaxiFareDescriptions,
)


@allure.feature("Taxi Fare Order")
@allure.story("Taxi fare selection and order form")
class TestTaxiFareOrder:
    """Test class for taxi fare order functionality.

    Test Scenario 4: Taxi Fare Order
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

    # Taxi Order Form Tests
    @allure.title("Verify taxi order form opens after Call Taxi")
    @allure.description(
        "Check that clicking Call Taxi button opens the taxi order form"
    )
    def test_taxi_order_form_opens(self, open_main_page):
        """Test that taxi order form is displayed."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify order form is displayed"):
            assert order_page.is_order_form_displayed(), (
                "Taxi order form should be displayed after clicking Call Taxi"
            )

    @allure.title("Verify taxi order form contains 6 fares")
    @allure.description(
        "Check that the form contains 6 fares according to specification"
    )
    def test_order_form_contains_six_fares(self, open_main_page):
        """Test that exactly 6 fares are displayed."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify 6 fares are displayed"):
            fares_count = order_page.get_fares_count()
            assert fares_count == 6, (
                f"Expected 6 fares, but found {fares_count}"
            )

    @allure.title("Verify exactly one fare is active by default")
    @allure.description(
        "Check that exactly one fare is selected by default"
    )
    def test_one_fare_active_by_default(self, open_main_page):
        """Test that one fare is preselected."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify exactly one fare is active"):
            assert order_page.is_one_fare_active(), (
                "Exactly one fare should be active by default"
            )

    @allure.title("Verify Business fare is available")
    @allure.description("Check that Business fare is displayed")
    def test_business_fare_available(self, open_main_page):
        """Test Business fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Business fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.BUSINESS), (
                "Business fare should be visible"
            )

    @allure.title("Verify Sleepy fare is available")
    @allure.description("Check that Sleepy fare is displayed")
    def test_sleepy_fare_available(self, open_main_page):
        """Test Sleepy fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Sleepy fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.SLEEPY), (
                "Sleepy fare should be visible"
            )

    @allure.title("Verify Vacation fare is available")
    @allure.description("Check that Vacation fare is displayed")
    def test_vacation_fare_available(self, open_main_page):
        """Test Vacation fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Vacation fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.VACATION), (
                "Vacation fare should be visible"
            )

    @allure.title("Verify Talkative fare is available")
    @allure.description("Check that Talkative fare is displayed")
    def test_talkative_fare_available(self, open_main_page):
        """Test Talkative fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Talkative fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.TALKATIVE), (
                "Talkative fare should be visible"
            )

    @allure.title("Verify Comforting fare is available")
    @allure.description("Check that Comforting fare is displayed")
    def test_comforting_fare_available(self, open_main_page):
        """Test Comforting fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Comforting fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.COMFORTING), (
                "Comforting fare should be visible"
            )

    @allure.title("Verify Glossy fare is available")
    @allure.description("Check that Glossy fare is displayed")
    def test_glossy_fare_available(self, open_main_page):
        """Test Glossy fare visibility."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify Glossy fare is visible"):
            assert order_page.is_fare_visible(TaxiFares.GLOSSY), (
                "Glossy fare should be visible"
            )

    @allure.title("Verify all 6 specified fares are present")
    @allure.description(
        "Check that all fares according to specification are displayed: "
        "Business, Sleepy, Vacation, Talkative, Comforting, Glossy"
    )
    def test_all_specified_fares_present(self, open_main_page):
        """Test that all specified fares are available."""
        _, _, order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify all fares are visible"):
            missing_fares = []
            for fare in TaxiFares.ALL_FARES:
                if not order_page.is_fare_visible(fare):
                    missing_fares.append(fare)

            assert not missing_fares, (
                f"Missing fares: {missing_fares}. "
                f"Expected all of: {TaxiFares.ALL_FARES}"
            )


@allure.feature("Taxi Fare Order")
@allure.story("Fare description tooltips")
class TestFareDescriptionTooltips:
    """Test class for fare description tooltip functionality."""

    def _navigate_to_taxi_order_form(self, driver):
        """Helper method to navigate to taxi order form."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()
        route_page.click_call_taxi()

        return OrderPage(driver)

    @allure.title("Verify Business fare tooltip text")
    @allure.description(
        "Check that hovering over Business fare info icon shows correct tooltip"
    )
    def test_business_fare_tooltip(self, open_main_page):
        """Test Business fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Business fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.BUSINESS)

        with allure.step("Verify tooltip is displayed"):
            assert order_page.is_tooltip_displayed(), (
                "Tooltip should be displayed on hover"
            )

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.BUSINESS
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Sleepy fare tooltip text")
    @allure.description(
        "Check that hovering over Sleepy fare info icon shows correct tooltip"
    )
    def test_sleepy_fare_tooltip(self, open_main_page):
        """Test Sleepy fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Sleepy fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.SLEEPY)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.SLEEPY
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Vacation fare tooltip text")
    @allure.description(
        "Check that hovering over Vacation fare info icon shows correct tooltip"
    )
    def test_vacation_fare_tooltip(self, open_main_page):
        """Test Vacation fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Vacation fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.VACATION)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.VACATION
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Talkative fare tooltip text")
    @allure.description(
        "Check that hovering over Talkative fare info icon shows correct tooltip"
    )
    def test_talkative_fare_tooltip(self, open_main_page):
        """Test Talkative fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Talkative fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.TALKATIVE)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.TALKATIVE
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Comforting fare tooltip text")
    @allure.description(
        "Check that hovering over Comforting fare info icon shows correct tooltip"
    )
    def test_comforting_fare_tooltip(self, open_main_page):
        """Test Comforting fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Comforting fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.COMFORTING)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.COMFORTING
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify Glossy fare tooltip text")
    @allure.description(
        "Check that hovering over Glossy fare info icon shows correct tooltip"
    )
    def test_glossy_fare_tooltip(self, open_main_page):
        """Test Glossy fare tooltip displays correct description."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Hover over Glossy fare info icon"):
            order_page.hover_fare_info_icon(TaxiFares.GLOSSY)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            expected = TaxiFareDescriptions.GLOSSY
            assert expected in tooltip_text, (
                f"Expected tooltip to contain '{expected}', but got '{tooltip_text}'"
            )

    @allure.title("Verify all fare tooltips match specification")
    @allure.description(
        "Check that all fare tooltips display text according to specification"
    )
    @pytest.mark.parametrize("fare,expected_description", [
        (TaxiFares.BUSINESS, TaxiFareDescriptions.BUSINESS),
        (TaxiFares.SLEEPY, TaxiFareDescriptions.SLEEPY),
        (TaxiFares.VACATION, TaxiFareDescriptions.VACATION),
        (TaxiFares.TALKATIVE, TaxiFareDescriptions.TALKATIVE),
        (TaxiFares.COMFORTING, TaxiFareDescriptions.COMFORTING),
        (TaxiFares.GLOSSY, TaxiFareDescriptions.GLOSSY),
    ])
    def test_fare_tooltip_parametrized(self, open_main_page, fare, expected_description):
        """Parametrized test for all fare tooltips."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step(f"Hover over {fare} fare info icon"):
            order_page.hover_fare_info_icon(fare)

        with allure.step("Verify tooltip text matches specification"):
            tooltip_text = order_page.get_tooltip_text()
            assert expected_description in tooltip_text, (
                f"For {fare} fare: expected '{expected_description}', "
                f"but got '{tooltip_text}'"
            )


@allure.feature("Taxi Fare Order")
@allure.story("Order form fields")
class TestTaxiOrderFormFields:
    """Test class for taxi order form fields."""

    def _navigate_to_taxi_order_form(self, driver):
        """Helper method to navigate to taxi order form."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_fast_route()
        route_page.click_call_taxi()

        return OrderPage(driver)

    @allure.title("Verify phone number field is present")
    @allure.description(
        "Check that the order form contains a phone number field"
    )
    def test_phone_field_present(self, open_main_page):
        """Test that phone number field is displayed."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify phone number field is displayed"):
            assert order_page.is_phone_field_displayed(), (
                "Phone number field should be present in the order form"
            )

    @allure.title("Verify payment method field is present")
    @allure.description(
        "Check that the order form contains a payment method field"
    )
    def test_payment_method_field_present(self, open_main_page):
        """Test that payment method field is displayed."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify payment method field is displayed"):
            assert order_page.is_payment_method_field_displayed(), (
                "Payment method field should be present in the order form"
            )

    @allure.title("Verify comment for driver field is present")
    @allure.description(
        "Check that the order form contains a comment for driver field"
    )
    def test_comment_field_present(self, open_main_page):
        """Test that comment field is displayed."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify comment field is displayed"):
            assert order_page.is_comment_field_displayed(), (
                "Comment for driver field should be present in the order form"
            )

    @allure.title("Verify order requirements field is present")
    @allure.description(
        "Check that the order form contains an order requirements field"
    )
    def test_requirements_field_present(self, open_main_page):
        """Test that requirements field is displayed."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify requirements field is displayed"):
            assert order_page.is_requirements_field_displayed(), (
                "Order requirements field should be present in the order form"
            )

    @allure.title("Verify all required form fields are present")
    @allure.description(
        "Check that the order form contains all required fields: "
        "phone, payment method, comment, and requirements"
    )
    def test_all_form_fields_present(self, open_main_page):
        """Test that all required fields are displayed."""
        order_page = self._navigate_to_taxi_order_form(open_main_page)

        with allure.step("Verify all form fields"):
            missing_fields = []

            if not order_page.is_phone_field_displayed():
                missing_fields.append("Phone number")

            if not order_page.is_payment_method_field_displayed():
                missing_fields.append("Payment method")

            if not order_page.is_comment_field_displayed():
                missing_fields.append("Comment for driver")

            if not order_page.is_requirements_field_displayed():
                missing_fields.append("Order requirements")

            assert not missing_fields, (
                f"Missing form fields: {missing_fields}"
            )
