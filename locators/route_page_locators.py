"""Locators for the Route Page."""

from selenium.webdriver.common.by import By


class RoutePageLocators:
    """Locators for Route Page elements."""

    # Route Options Block
    ROUTE_OPTIONS_BLOCK = (By.CLASS_NAME, "route-options")
    ROUTE_DISTANCE = (By.CLASS_NAME, "route-distance")
    ROUTE_DURATION = (By.CLASS_NAME, "route-duration")
    ROUTE_COST = (By.CLASS_NAME, "route-cost")
    ROUTE_TRAVEL_TIME = (By.CLASS_NAME, "route-travel-time")

    # Route Type Tabs
    ROUTE_TYPE_SELECTOR = (By.CLASS_NAME, "route-type-selector")
    OPTIMAL_TAB = (By.CSS_SELECTOR, "[data-route-type='optimal']")
    FAST_TAB = (By.CSS_SELECTOR, "[data-route-type='fast']")
    CUSTOM_TAB = (By.CSS_SELECTOR, "[data-route-type='custom']")
    ACTIVE_ROUTE_TAB = (By.CSS_SELECTOR, ".route-type-tab.active, [data-route-type].active")

    # Transport Types (for Custom route)
    TRANSPORT_TYPE_SELECTOR = (By.CLASS_NAME, "transport-selector")
    CAR_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='car']")
    WALKING_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='walking']")
    TAXI_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='taxi']")
    BICYCLE_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='bicycle']")
    SCOOTER_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='scooter']")
    DRIVE_TRANSPORT = (By.CSS_SELECTOR, "[data-transport='drive']")
    ACTIVE_TRANSPORT = (By.CSS_SELECTOR, ".transport-option.active, [data-transport].active")

    # Legacy locators for compatibility
    ROUTE_MODE_SELECTOR = (By.CLASS_NAME, "mode-selector")
    WALKING_MODE = (By.CSS_SELECTOR, "[data-mode='walking']")
    DRIVING_MODE = (By.CSS_SELECTOR, "[data-mode='driving']")
    TRANSIT_MODE = (By.CSS_SELECTOR, "[data-mode='transit']")

    # Action Buttons
    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, ".call-taxi-button, [data-action='call-taxi']")
    BOOK_BUTTON = (By.CSS_SELECTOR, ".book-button, [data-action='book']")

    # Same Address Display
    ROUTE_TYPE_TEXT = (By.CLASS_NAME, "route-type-text")
    COST_TEXT = (By.CLASS_NAME, "cost-text")
