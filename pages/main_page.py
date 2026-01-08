import allure
from selenium.webdriver.common.by import By
from pages.base_object import BaseObject


class MainPage(BaseObject):
    """Page Object for the Main Page with address input fields."""

    # Locators
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    BUILD_ROUTE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ROUTE_INFO = (By.CLASS_NAME, "route-info")
    ORDER_TAXI_BUTTON = (By.CSS_SELECTOR, ".order-button")
    MAP_CONTAINER = (By.ID, "map")
    LOADER = (By.CLASS_NAME, "loader")

    @allure.step("Enter 'From' address: {address}")
    def enter_from_address(self, address: str) -> None:
        """Enter the departure address."""
        self.send_keys(self.FROM_INPUT, address)

    @allure.step("Enter 'To' address: {address}")
    def enter_to_address(self, address: str) -> None:
        """Enter the destination address."""
        self.send_keys(self.TO_INPUT, address)

    @allure.step("Click 'Build Route' button")
    def click_build_route(self) -> None:
        """Click the button to build the route."""
        self.click(self.BUILD_ROUTE_BUTTON)

    @allure.step("Build route from '{from_address}' to '{to_address}'")
    def build_route(self, from_address: str, to_address: str) -> None:
        """Complete flow to build a route."""
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)
        self.click_build_route()
        self.wait_for_route_to_be_built()

    @allure.step("Wait for route to be built")
    def wait_for_route_to_be_built(self) -> None:
        """Wait for the route calculation to complete."""
        self.wait_for_element_visible(self.ROUTE_INFO)

    @allure.step("Check if route info is displayed")
    def is_route_info_displayed(self) -> bool:
        """Verify if route information is visible."""
        return self.is_element_visible(self.ROUTE_INFO)

    @allure.step("Get route info text")
    def get_route_info_text(self) -> str:
        """Get the text from route info block."""
        return self.get_text(self.ROUTE_INFO)

    @allure.step("Check if 'Order Taxi' button is displayed")
    def is_order_taxi_button_displayed(self) -> bool:
        """Check if the order taxi button is visible."""
        return self.is_element_visible(self.ORDER_TAXI_BUTTON)

    @allure.step("Click 'Order Taxi' button")
    def click_order_taxi(self) -> None:
        """Click the order taxi button."""
        self.click(self.ORDER_TAXI_BUTTON)

    @allure.step("Check if map is displayed")
    def is_map_displayed(self) -> bool:
        """Verify if the map container is visible."""
        return self.is_element_visible(self.MAP_CONTAINER)

    @allure.step("Get 'From' input value")
    def get_from_input_value(self) -> str:
        """Get the current value of the 'From' input field."""
        return self.get_attribute(self.FROM_INPUT, "value")

    @allure.step("Get 'To' input value")
    def get_to_input_value(self) -> str:
        """Get the current value of the 'To' input field."""
        return self.get_attribute(self.TO_INPUT, "value")

    @allure.step("Wait for page to load using JavaScript")
    def wait_for_page_load(self) -> None:
        """Use JavaScript to wait for the page to fully load."""
        self.execute_script(
            "return new Promise(resolve => setTimeout(resolve, 500));"
        )

    @allure.step("Hover over map container")
    def hover_over_map(self) -> None:
        """Hover over the map element."""
        self.hover(self.MAP_CONTAINER)
