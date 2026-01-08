"""Locators for the Main Page."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators for Main Page elements."""

    # Address Input
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    BUILD_ROUTE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ROUTE_INFO = (By.CLASS_NAME, "route-info")
    ORDER_TAXI_BUTTON = (By.CSS_SELECTOR, ".order-button")
    LOADER = (By.CLASS_NAME, "loader")

    # Map
    MAP_CONTAINER = (By.ID, "map")
    START_MARKER = (By.CSS_SELECTOR, ".map-marker-start, [data-marker='start']")
    END_MARKER = (By.CSS_SELECTOR, ".map-marker-end, [data-marker='end']")
    ROUTE_LINE = (By.CSS_SELECTOR, ".route-line, .map-route")
