import allure
from selenium.webdriver.common.by import By
from pages.base_object import BaseObject


class OrderPage(BaseObject):
    """Page Object for the Taxi Order Page."""

    # Locators
    ORDER_FORM = (By.CLASS_NAME, "order-form")
    TARIFF_SELECTOR = (By.CLASS_NAME, "tariff-selector")
    ECONOMY_TARIFF = (By.CSS_SELECTOR, "[data-tariff='economy']")
    COMFORT_TARIFF = (By.CSS_SELECTOR, "[data-tariff='comfort']")
    BUSINESS_TARIFF = (By.CSS_SELECTOR, "[data-tariff='business']")
    PHONE_INPUT = (By.ID, "phone")
    COMMENT_INPUT = (By.ID, "comment")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".confirm-order")
    ORDER_PRICE = (By.CLASS_NAME, "order-price")
    PAYMENT_METHOD_SELECTOR = (By.CLASS_NAME, "payment-method")
    CARD_PAYMENT = (By.CSS_SELECTOR, "[data-payment='card']")
    CASH_PAYMENT = (By.CSS_SELECTOR, "[data-payment='cash']")

    @allure.step("Check if order form is displayed")
    def is_order_form_displayed(self) -> bool:
        """Verify if order form is visible."""
        return self.is_element_visible(self.ORDER_FORM)

    @allure.step("Select economy tariff")
    def select_economy_tariff(self) -> None:
        """Select economy tariff."""
        self.click(self.ECONOMY_TARIFF)

    @allure.step("Select comfort tariff")
    def select_comfort_tariff(self) -> None:
        """Select comfort tariff."""
        self.click(self.COMFORT_TARIFF)

    @allure.step("Select business tariff")
    def select_business_tariff(self) -> None:
        """Select business tariff."""
        self.click(self.BUSINESS_TARIFF)

    @allure.step("Enter phone number: {phone}")
    def enter_phone(self, phone: str) -> None:
        """Enter phone number in the order form."""
        self.send_keys(self.PHONE_INPUT, phone)

    @allure.step("Enter comment: {comment}")
    def enter_comment(self, comment: str) -> None:
        """Enter a comment for the order."""
        self.send_keys(self.COMMENT_INPUT, comment)

    @allure.step("Click confirm order button")
    def click_confirm_order(self) -> None:
        """Click the button to confirm the order."""
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Get order price")
    def get_order_price(self) -> str:
        """Get the displayed order price."""
        return self.get_text(self.ORDER_PRICE)

    @allure.step("Select card payment method")
    def select_card_payment(self) -> None:
        """Select card as payment method."""
        self.click(self.CARD_PAYMENT)

    @allure.step("Select cash payment method")
    def select_cash_payment(self) -> None:
        """Select cash as payment method."""
        self.click(self.CASH_PAYMENT)

    @allure.step("Hover over tariff selector")
    def hover_over_tariff_selector(self) -> None:
        """Hover over the tariff selector."""
        self.hover(self.TARIFF_SELECTOR)
