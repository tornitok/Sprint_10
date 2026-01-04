"""
Локаторы для главной страницы сервиса EZ Route.
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""

    # Поля ввода адресов
    FROM_FIELD = (By.XPATH, "//input[@id='from']")
    TO_FIELD = (By.XPATH, "//input[@id='to']")

    # Выпадающие списки с предустановленными адресами
    FROM_SUGGESTIONS = (By.CSS_SELECTOR, ".from-suggestions .suggestion-item")
    TO_SUGGESTIONS = (By.CSS_SELECTOR, ".to-suggestions .suggestion-item")

    # Элементы карты
    MAP_CONTAINER = (By.ID, "map")
    ROUTE_START_POINT = (By.CSS_SELECTOR, ".route-point-from")
    ROUTE_END_POINT = (By.CSS_SELECTOR, ".route-point-to")
    ROUTE_LINE = (By.CSS_SELECTOR, ".route-line")

    # Маркеры на карте (возможные варианты селекторов)
    MAP_MARKERS = (By.CSS_SELECTOR, ".leaflet-marker-icon, .map-marker, [class*='marker']")
    ROUTE_POINTS = (By.CSS_SELECTOR, "[class*='route-point'], [class*='waypoint']")

    # Блок выбора маршрута
    ROUTE_SELECTION_BLOCK = (By.XPATH, "//div[@class='results-text']")
    ROUTE_INFO_TEXT = (By.CSS_SELECTOR, ".route-selection *, .route-info *, [class*='route-select'] *, [class*='route-info'] *")

