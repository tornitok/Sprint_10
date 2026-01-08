import allure
from selenium.webdriver.common.by import By
from pages.base_object import BaseObject
from locators.order_page_locators import OrderPageLocators


class OrderPage(BaseObject):
    """Page Object for the Taxi Order Page."""

    @allure.step("Check if order form is displayed")
    def is_order_form_displayed(self) -> bool:
        """Verify if order form is visible."""
        return self.is_element_visible(OrderPageLocators.ORDER_FORM)

    @allure.step("Select economy tariff")
    def select_economy_tariff(self) -> None:
        """Select economy tariff."""
        self.click(OrderPageLocators.ECONOMY_TARIFF)

    @allure.step("Select comfort tariff")
    def select_comfort_tariff(self) -> None:
        """Select comfort tariff."""
        self.click(OrderPageLocators.COMFORT_TARIFF)

    @allure.step("Select business tariff")
    def select_business_tariff(self) -> None:
        """Select business tariff."""
        self.click(OrderPageLocators.BUSINESS_TARIFF)

    @allure.step("Enter phone number: {phone}")
    def enter_phone(self, phone: str) -> None:
        """Enter phone number in the order form."""
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Enter comment: {comment}")
    def enter_comment(self, comment: str) -> None:
        """Enter a comment for the order."""
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Click confirm order button")
    def click_confirm_order(self) -> None:
        """Click the button to confirm the order."""
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Get order price")
    def get_order_price(self) -> str:
        """Get the displayed order price."""
        return self.get_text(OrderPageLocators.ORDER_PRICE)

    @allure.step("Select card payment method")
    def select_card_payment(self) -> None:
        """Select card as payment method."""
        self.click(OrderPageLocators.CARD_PAYMENT)

    @allure.step("Select cash payment method")
    def select_cash_payment(self) -> None:
        """Select cash as payment method."""
        self.click(OrderPageLocators.CASH_PAYMENT)

    @allure.step("Hover over tariff selector")
    def hover_over_tariff_selector(self) -> None:
        """Hover over the tariff selector."""
        self.hover(OrderPageLocators.TARIFF_SELECTOR)

    # Taxi Fare Methods
    @allure.step("Select Business fare")
    def select_business_fare(self) -> None:
        """Select Business taxi fare."""
        self.click(OrderPageLocators.BUSINESS_FARE)

    @allure.step("Select Sleepy fare")
    def select_sleepy_fare(self) -> None:
        """Select Sleepy taxi fare."""
        self.click(OrderPageLocators.SLEEPY_FARE)

    @allure.step("Select Vacation fare")
    def select_vacation_fare(self) -> None:
        """Select Vacation taxi fare."""
        self.click(OrderPageLocators.VACATION_FARE)

    @allure.step("Select Talkative fare")
    def select_talkative_fare(self) -> None:
        """Select Talkative taxi fare."""
        self.click(OrderPageLocators.TALKATIVE_FARE)

    @allure.step("Select Comforting fare")
    def select_comforting_fare(self) -> None:
        """Select Comforting taxi fare."""
        self.click(OrderPageLocators.COMFORTING_FARE)

    @allure.step("Select Glossy fare")
    def select_glossy_fare(self) -> None:
        """Select Glossy taxi fare."""
        self.click(OrderPageLocators.GLOSSY_FARE)

    @allure.step("Get all displayed fares count")
    def get_fares_count(self) -> int:
        """Get count of displayed taxi fares."""
        elements = self.find_elements(OrderPageLocators.ALL_FARES)
        return len(elements)

    @allure.step("Check if exactly one fare is active")
    def is_one_fare_active(self) -> bool:
        """Check if exactly one fare is selected by default."""
        elements = self.find_elements(OrderPageLocators.ACTIVE_FARE)
        return len(elements) == 1

    @allure.step("Get active fare name")
    def get_active_fare_name(self) -> str:
        """Get the name of the currently active fare."""
        element = self.find_element(OrderPageLocators.ACTIVE_FARE)
        return element.get_attribute("data-fare")

    @allure.step("Check if fare is visible: {fare_name}")
    def is_fare_visible(self, fare_name: str) -> bool:
        """Check if a specific fare is visible."""
        locator = (By.CSS_SELECTOR, f"[data-fare='{fare_name.lower()}']")
        return self.is_element_visible(locator)

    # Fare Tooltip Methods
    @allure.step("Hover over fare info icon for fare: {fare_name}")
    def hover_fare_info_icon(self, fare_name: str) -> None:
        """Hover over the info icon for a specific fare."""
        locator = (By.CSS_SELECTOR, f"[data-fare='{fare_name.lower()}'] .fare-info-icon")
        self.hover(locator)

    @allure.step("Get tooltip text")
    def get_tooltip_text(self) -> str:
        """Get the text from the displayed tooltip."""
        return self.get_text(OrderPageLocators.FARE_TOOLTIP)

    @allure.step("Check if tooltip is displayed")
    def is_tooltip_displayed(self) -> bool:
        """Check if tooltip is visible."""
        return self.is_element_visible(OrderPageLocators.FARE_TOOLTIP)

    # Order Form Field Methods
    @allure.step("Check if phone field is displayed")
    def is_phone_field_displayed(self) -> bool:
        """Check if phone number field is visible."""
        return (self.is_element_visible(OrderPageLocators.PHONE_FIELD) or
                self.is_element_visible(OrderPageLocators.PHONE_INPUT))

    @allure.step("Check if payment method field is displayed")
    def is_payment_method_field_displayed(self) -> bool:
        """Check if payment method field is visible."""
        return (self.is_element_visible(OrderPageLocators.PAYMENT_METHOD_FIELD) or
                self.is_element_visible(OrderPageLocators.PAYMENT_METHOD_SELECTOR))

    @allure.step("Check if comment field is displayed")
    def is_comment_field_displayed(self) -> bool:
        """Check if comment for driver field is visible."""
        return (self.is_element_visible(OrderPageLocators.COMMENT_FIELD) or
                self.is_element_visible(OrderPageLocators.COMMENT_INPUT))

    @allure.step("Check if requirements field is displayed")
    def is_requirements_field_displayed(self) -> bool:
        """Check if order requirements field is visible."""
        return self.is_element_visible(OrderPageLocators.REQUIREMENTS_FIELD)

    # Order Requirements Methods
    @allure.step("Enable Laptop table checkbox")
    def enable_laptop_table(self) -> None:
        """Enable the Laptop table requirement checkbox."""
        self.click(OrderPageLocators.LAPTOP_TABLE_CHECKBOX)

    @allure.step("Check if Laptop table is selected")
    def is_laptop_table_selected(self) -> bool:
        """Check if Laptop table checkbox is selected."""
        element = self.find_element(OrderPageLocators.LAPTOP_TABLE_CHECKBOX)
        return element.is_selected()

    # Order Action Methods
    @allure.step("Click 'Enter number and order' button")
    def click_enter_number_and_order(self) -> None:
        """Click the Enter number and order button."""
        self.click(OrderPageLocators.ENTER_NUMBER_ORDER_BUTTON)

    @allure.step("Click Cancel button")
    def click_cancel(self) -> None:
        """Click the Cancel button."""
        self.click(OrderPageLocators.CANCEL_BUTTON)

    @allure.step("Click Details button")
    def click_details(self) -> None:
        """Click the Details button."""
        self.click(OrderPageLocators.DETAILS_BUTTON)

    # Car Search Window Methods
    @allure.step("Check if car search window is displayed")
    def is_car_search_window_displayed(self) -> bool:
        """Check if car search window is visible."""
        return self.is_element_visible(OrderPageLocators.CAR_SEARCH_WINDOW)

    @allure.step("Get car search title")
    def get_car_search_title(self) -> str:
        """Get the title of the car search window."""
        return self.get_text(OrderPageLocators.CAR_SEARCH_TITLE)

    @allure.step("Check if search timer is displayed")
    def is_search_timer_displayed(self) -> bool:
        """Check if countdown timer is visible."""
        return self.is_element_visible(OrderPageLocators.CAR_SEARCH_TIMER)

    @allure.step("Wait for car search to complete")
    def wait_for_search_complete(self, timeout: int = 60) -> None:
        """Wait for car search timer to finish."""
        self.wait_for_element_invisible(OrderPageLocators.CAR_SEARCH_TIMER, timeout)

    # Completed Order Window Methods
    @allure.step("Check if completed order window is displayed")
    def is_completed_order_displayed(self) -> bool:
        """Check if completed order window is visible."""
        return self.is_element_visible(OrderPageLocators.COMPLETED_ORDER_WINDOW)

    @allure.step("Get order title")
    def get_order_title(self) -> str:
        """Get the order title (e.g., 'N minutes and arriving')."""
        return self.get_text(OrderPageLocators.ORDER_TITLE)

    @allure.step("Check if car number is displayed")
    def is_car_number_displayed(self) -> bool:
        """Check if car number is visible."""
        return self.is_element_visible(OrderPageLocators.CAR_NUMBER)

    @allure.step("Get car number")
    def get_car_number(self) -> str:
        """Get the car number."""
        return self.get_text(OrderPageLocators.CAR_NUMBER)

    @allure.step("Check if fare image is displayed")
    def is_fare_image_displayed(self) -> bool:
        """Check if fare image is visible."""
        return self.is_element_visible(OrderPageLocators.FARE_IMAGE)

    # Driver Info Methods
    @allure.step("Check if driver info is displayed")
    def is_driver_info_displayed(self) -> bool:
        """Check if driver info block is visible."""
        return self.is_element_visible(OrderPageLocators.DRIVER_INFO_BLOCK)

    @allure.step("Get driver name")
    def get_driver_name(self) -> str:
        """Get the driver name."""
        return self.get_text(OrderPageLocators.DRIVER_NAME)

    @allure.step("Check if driver photo is displayed")
    def is_driver_photo_displayed(self) -> bool:
        """Check if driver photo is visible."""
        return self.is_element_visible(OrderPageLocators.DRIVER_PHOTO)

    @allure.step("Get driver rating")
    def get_driver_rating(self) -> str:
        """Get the driver rating."""
        return self.get_text(OrderPageLocators.DRIVER_RATING)

    # Order Details Methods
    @allure.step("Check if order details window is displayed")
    def is_order_details_displayed(self) -> bool:
        """Check if order details window is visible."""
        return self.is_element_visible(OrderPageLocators.ORDER_DETAILS_WINDOW)

    @allure.step("Get pickup address from details")
    def get_pickup_address(self) -> str:
        """Get the pickup address from order details."""
        return self.get_text(OrderPageLocators.PICKUP_ADDRESS)

    @allure.step("Get destination address from details")
    def get_destination_address(self) -> str:
        """Get the destination address from order details."""
        return self.get_text(OrderPageLocators.DESTINATION_ADDRESS)

    @allure.step("Get payment method from details")
    def get_payment_method_display(self) -> str:
        """Get the payment method from order details."""
        return self.get_text(OrderPageLocators.PAYMENT_METHOD_DISPLAY)

    @allure.step("Get trip cost from details")
    def get_trip_cost(self) -> str:
        """Get the trip cost from order details."""
        return self.get_text(OrderPageLocators.TRIP_COST)

    @allure.step("Check if order window is closed")
    def is_order_window_closed(self) -> bool:
        """Check if order window has been closed."""
        return not self.is_element_visible(OrderPageLocators.COMPLETED_ORDER_WINDOW, timeout=3)

    # Drive Order Methods
    @allure.step("Check if drive order form is displayed")
    def is_drive_order_form_displayed(self) -> bool:
        """Check if drive order form is visible."""
        return self.is_element_visible(OrderPageLocators.DRIVE_ORDER_FORM)

    @allure.step("Select Everyday fare")
    def select_everyday_fare(self) -> None:
        """Select Everyday drive fare."""
        self.click(OrderPageLocators.EVERYDAY_FARE)

    @allure.step("Select Outdoor fare")
    def select_outdoor_fare(self) -> None:
        """Select Outdoor drive fare."""
        self.click(OrderPageLocators.OUTDOOR_FARE)

    @allure.step("Select Luxury fare")
    def select_luxury_fare(self) -> None:
        """Select Luxury drive fare."""
        self.click(OrderPageLocators.LUXURY_FARE)

    # Driver License Methods
    @allure.step("Check if license window is displayed")
    def is_license_window_displayed(self) -> bool:
        """Check if add driver license window is visible."""
        return self.is_element_visible(OrderPageLocators.LICENSE_WINDOW)

    @allure.step("Enter first name: {first_name}")
    def enter_first_name(self, first_name: str) -> None:
        """Enter first name in license form."""
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step("Enter last name: {last_name}")
    def enter_last_name(self, last_name: str) -> None:
        """Enter last name in license form."""
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Enter date of birth: {dob}")
    def enter_date_of_birth(self, dob: str) -> None:
        """Enter date of birth in license form."""
        self.send_keys(OrderPageLocators.DATE_OF_BIRTH_INPUT, dob)

    @allure.step("Enter license number: {license_num}")
    def enter_license_number(self, license_num: str) -> None:
        """Enter license number in license form."""
        self.send_keys(OrderPageLocators.LICENSE_NUMBER_INPUT, license_num)

    @allure.step("Click Add license button")
    def click_add_license(self) -> None:
        """Click the Add button in license form."""
        self.click(OrderPageLocators.ADD_LICENSE_BUTTON)

    @allure.step("Click Cancel license button")
    def click_cancel_license(self) -> None:
        """Click the Cancel button in license form."""
        self.click(OrderPageLocators.CANCEL_LICENSE_BUTTON)

    @allure.step("Check if first name field is displayed")
    def is_first_name_field_displayed(self) -> bool:
        """Check if first name field is visible in license form."""
        return self.is_element_visible(OrderPageLocators.FIRST_NAME_INPUT)

    @allure.step("Check if last name field is displayed")
    def is_last_name_field_displayed(self) -> bool:
        """Check if last name field is visible in license form."""
        return self.is_element_visible(OrderPageLocators.LAST_NAME_INPUT)

    @allure.step("Check if date of birth field is displayed")
    def is_date_of_birth_field_displayed(self) -> bool:
        """Check if date of birth field is visible in license form."""
        return self.is_element_visible(OrderPageLocators.DATE_OF_BIRTH_INPUT)

    @allure.step("Check if license number field is displayed")
    def is_license_number_field_displayed(self) -> bool:
        """Check if license number field is visible in license form."""
        return self.is_element_visible(OrderPageLocators.LICENSE_NUMBER_INPUT)

    # Completed Drive Order Methods
    @allure.step("Check if drive order window is displayed")
    def is_drive_order_window_displayed(self) -> bool:
        """Check if completed drive order window is visible."""
        return self.is_element_visible(OrderPageLocators.DRIVE_ORDER_WINDOW)

    @allure.step("Check if free waiting timer is displayed")
    def is_free_waiting_timer_displayed(self) -> bool:
        """Check if free waiting timer is visible."""
        return self.is_element_visible(OrderPageLocators.FREE_WAITING_TIMER)

    @allure.step("Get car location address")
    def get_car_location_address(self) -> str:
        """Get the car location address (From)."""
        return self.get_text(OrderPageLocators.CAR_LOCATION_ADDRESS)
