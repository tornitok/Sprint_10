"""Локаторы для главной страницы."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы."""

    # Поля ввода адресов
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    ROUTE_INFO = (By.CSS_SELECTOR, ".results-container")
    ORDER_TAXI_BUTTON = (By.CSS_SELECTOR, ".order-button, .results-text button")
    LOADER = (By.CLASS_NAME, "loader")

    # Карта
    MAP_CONTAINER = (By.CLASS_NAME, "map")
    START_MARKER = (By.CSS_SELECTOR, ".ymaps-2-1-79-route-pin, [class*='route-pin']")
    END_MARKER = (By.CSS_SELECTOR, ".ymaps-2-1-79-route-pin, [class*='route-pin']")
    ROUTE_LINE = (By.CSS_SELECTOR, "[class*='routerPoints-pane'], [class*='route-line']")
