import allure
from selenium.webdriver.common.by import By
from pages.base_object import BaseObject


class RoutePage(BaseObject):
    """Page Object for the Route Page with route options."""

    # Locators
    ROUTE_OPTIONS_BLOCK = (By.CLASS_NAME, "route-options")
    ROUTE_DISTANCE = (By.CLASS_NAME, "route-distance")
    ROUTE_DURATION = (By.CLASS_NAME, "route-duration")
    ROUTE_MODE_SELECTOR = (By.CLASS_NAME, "mode-selector")
    WALKING_MODE = (By.CSS_SELECTOR, "[data-mode='walking']")
    DRIVING_MODE = (By.CSS_SELECTOR, "[data-mode='driving']")
    TRANSIT_MODE = (By.CSS_SELECTOR, "[data-mode='transit']")

    @allure.step("Check if route options block is displayed")
    def is_route_options_displayed(self) -> bool:
        """Verify if route options block is visible."""
        return self.is_element_visible(self.ROUTE_OPTIONS_BLOCK)

    @allure.step("Get route distance")
    def get_route_distance(self) -> str:
        """Get the displayed route distance."""
        return self.get_text(self.ROUTE_DISTANCE)

    @allure.step("Get route duration")
    def get_route_duration(self) -> str:
        """Get the displayed route duration."""
        return self.get_text(self.ROUTE_DURATION)

    @allure.step("Select walking mode")
    def select_walking_mode(self) -> None:
        """Select walking as the route mode."""
        self.click(self.WALKING_MODE)

    @allure.step("Select driving mode")
    def select_driving_mode(self) -> None:
        """Select driving as the route mode."""
        self.click(self.DRIVING_MODE)

    @allure.step("Select transit mode")
    def select_transit_mode(self) -> None:
        """Select transit as the route mode."""
        self.click(self.TRANSIT_MODE)

    @allure.step("Hover over route options")
    def hover_over_route_options(self) -> None:
        """Hover over the route options block."""
        self.hover(self.ROUTE_OPTIONS_BLOCK)
