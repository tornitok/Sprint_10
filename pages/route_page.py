import allure
from pages.base_object import BaseObject
from locators.route_page_locators import RoutePageLocators


class RoutePage(BaseObject):
    """Page Object for the Route Page with route options."""

    @allure.step("Check if route options block is displayed")
    def is_route_options_displayed(self) -> bool:
        """Verify if route options block is visible."""
        return self.is_element_visible(RoutePageLocators.ROUTE_OPTIONS_BLOCK)

    @allure.step("Get route distance")
    def get_route_distance(self) -> str:
        """Get the displayed route distance."""
        return self.get_text(RoutePageLocators.ROUTE_DISTANCE)

    @allure.step("Get route duration")
    def get_route_duration(self) -> str:
        """Get the displayed route duration."""
        return self.get_text(RoutePageLocators.ROUTE_DURATION)

    @allure.step("Select walking mode")
    def select_walking_mode(self) -> None:
        """Select walking as the route mode."""
        self.click(RoutePageLocators.WALKING_MODE)

    @allure.step("Select driving mode")
    def select_driving_mode(self) -> None:
        """Select driving as the route mode."""
        self.click(RoutePageLocators.DRIVING_MODE)

    @allure.step("Select transit mode")
    def select_transit_mode(self) -> None:
        """Select transit as the route mode."""
        self.click(RoutePageLocators.TRANSIT_MODE)

    @allure.step("Hover over route options")
    def hover_over_route_options(self) -> None:
        """Hover over the route options block."""
        self.hover(RoutePageLocators.ROUTE_OPTIONS_BLOCK)

    # Route Type Tab Methods
    @allure.step("Select Optimal route tab")
    def select_optimal_route(self) -> None:
        """Select the Optimal route type tab."""
        self.click(RoutePageLocators.OPTIMAL_TAB)

    @allure.step("Select Fast route tab")
    def select_fast_route(self) -> None:
        """Select the Fast route type tab."""
        self.click(RoutePageLocators.FAST_TAB)

    @allure.step("Select Custom route tab")
    def select_custom_route(self) -> None:
        """Select the Custom route type tab."""
        self.click(RoutePageLocators.CUSTOM_TAB)

    @allure.step("Get active route tab text")
    def get_active_route_tab_text(self) -> str:
        """Get the text of the currently active route tab."""
        return self.get_text(RoutePageLocators.ACTIVE_ROUTE_TAB)

    @allure.step("Check if Optimal tab is active")
    def is_optimal_tab_active(self) -> bool:
        """Check if Optimal route tab is active."""
        element = self.find_element(RoutePageLocators.OPTIMAL_TAB)
        return "active" in element.get_attribute("class")

    @allure.step("Check if Fast tab is active")
    def is_fast_tab_active(self) -> bool:
        """Check if Fast route tab is active."""
        element = self.find_element(RoutePageLocators.FAST_TAB)
        return "active" in element.get_attribute("class")

    @allure.step("Check if Custom tab is active")
    def is_custom_tab_active(self) -> bool:
        """Check if Custom route tab is active."""
        element = self.find_element(RoutePageLocators.CUSTOM_TAB)
        return "active" in element.get_attribute("class")

    # Transport Type Methods
    @allure.step("Select Car transport")
    def select_car_transport(self) -> None:
        """Select Car as transport type."""
        self.click(RoutePageLocators.CAR_TRANSPORT)

    @allure.step("Select Walking transport")
    def select_walking_transport(self) -> None:
        """Select Walking as transport type."""
        self.click(RoutePageLocators.WALKING_TRANSPORT)

    @allure.step("Select Taxi transport")
    def select_taxi_transport(self) -> None:
        """Select Taxi as transport type."""
        self.click(RoutePageLocators.TAXI_TRANSPORT)

    @allure.step("Select Bicycle transport")
    def select_bicycle_transport(self) -> None:
        """Select Bicycle as transport type."""
        self.click(RoutePageLocators.BICYCLE_TRANSPORT)

    @allure.step("Select Scooter transport")
    def select_scooter_transport(self) -> None:
        """Select Scooter as transport type."""
        self.click(RoutePageLocators.SCOOTER_TRANSPORT)

    @allure.step("Select Drive transport")
    def select_drive_transport(self) -> None:
        """Select Drive as transport type."""
        self.click(RoutePageLocators.DRIVE_TRANSPORT)

    @allure.step("Check if transport selector is displayed")
    def is_transport_selector_displayed(self) -> bool:
        """Check if transport type selector is visible."""
        return self.is_element_visible(RoutePageLocators.TRANSPORT_TYPE_SELECTOR)

    @allure.step("Check if Car transport is active")
    def is_car_transport_active(self) -> bool:
        """Check if Car transport is active."""
        return self.is_element_visible(RoutePageLocators.CAR_TRANSPORT)

    @allure.step("Check if Walking transport is active")
    def is_walking_transport_visible(self) -> bool:
        """Check if Walking transport option is visible."""
        return self.is_element_visible(RoutePageLocators.WALKING_TRANSPORT)

    @allure.step("Check if Taxi transport is visible")
    def is_taxi_transport_visible(self) -> bool:
        """Check if Taxi transport option is visible."""
        return self.is_element_visible(RoutePageLocators.TAXI_TRANSPORT)

    @allure.step("Check if Bicycle transport is visible")
    def is_bicycle_transport_visible(self) -> bool:
        """Check if Bicycle transport option is visible."""
        return self.is_element_visible(RoutePageLocators.BICYCLE_TRANSPORT)

    @allure.step("Check if Scooter transport is visible")
    def is_scooter_transport_visible(self) -> bool:
        """Check if Scooter transport option is visible."""
        return self.is_element_visible(RoutePageLocators.SCOOTER_TRANSPORT)

    @allure.step("Check if Drive transport is visible")
    def is_drive_transport_visible(self) -> bool:
        """Check if Drive transport option is visible."""
        return self.is_element_visible(RoutePageLocators.DRIVE_TRANSPORT)

    # Button Methods
    @allure.step("Check if Call Taxi button is displayed")
    def is_call_taxi_button_displayed(self) -> bool:
        """Check if Call Taxi button is visible."""
        return self.is_element_visible(RoutePageLocators.CALL_TAXI_BUTTON)

    @allure.step("Check if Call Taxi button is enabled")
    def is_call_taxi_button_enabled(self) -> bool:
        """Check if Call Taxi button is enabled."""
        element = self.find_element(RoutePageLocators.CALL_TAXI_BUTTON)
        return element.is_enabled()

    @allure.step("Click Call Taxi button")
    def click_call_taxi(self) -> None:
        """Click the Call Taxi button."""
        self.click(RoutePageLocators.CALL_TAXI_BUTTON)

    @allure.step("Check if Book button is displayed")
    def is_book_button_displayed(self) -> bool:
        """Check if Book button is visible."""
        return self.is_element_visible(RoutePageLocators.BOOK_BUTTON)

    @allure.step("Check if Book button is enabled")
    def is_book_button_enabled(self) -> bool:
        """Check if Book button is enabled."""
        element = self.find_element(RoutePageLocators.BOOK_BUTTON)
        return element.is_enabled()

    @allure.step("Click Book button")
    def click_book(self) -> None:
        """Click the Book button."""
        self.click(RoutePageLocators.BOOK_BUTTON)

    # Cost and Time Methods
    @allure.step("Get route cost")
    def get_route_cost(self) -> str:
        """Get the displayed route cost."""
        return self.get_text(RoutePageLocators.ROUTE_COST)

    @allure.step("Get route travel time")
    def get_route_travel_time(self) -> str:
        """Get the displayed travel time."""
        return self.get_text(RoutePageLocators.ROUTE_TRAVEL_TIME)

    @allure.step("Get route type text")
    def get_route_type_text(self) -> str:
        """Get the route type text."""
        return self.get_text(RoutePageLocators.ROUTE_TYPE_TEXT)

    @allure.step("Get cost text")
    def get_cost_text(self) -> str:
        """Get the cost text."""
        return self.get_text(RoutePageLocators.COST_TEXT)
