"""Локаторы для страницы маршрута."""

from selenium.webdriver.common.by import By


class RoutePageLocators:
    """Локаторы элементов страницы маршрута."""

    # Блок выбора маршрута
    ROUTE_OPTIONS_BLOCK = (By.CSS_SELECTOR, ".type-picker.shown")
    ROUTE_DISTANCE = (By.CLASS_NAME, "route-distance")
    ROUTE_DURATION = (By.CLASS_NAME, "duration")
    ROUTE_COST = (By.CSS_SELECTOR, ".text")
    ROUTE_TRAVEL_TIME = (By.CLASS_NAME, "duration")

    # Виды маршрута (Оптимальный, Быстрый, Свой)
    ROUTE_TYPE_SELECTOR = (By.CLASS_NAME, "modes-container")
    OPTIMAL_TAB = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Оптимальный')]")
    FAST_TAB = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Быстрый')]")
    CUSTOM_TAB = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Свой')]")
    ACTIVE_ROUTE_TAB = (By.CSS_SELECTOR, ".mode.active")

    # Типы передвижения (для маршрута Свой)
    TRANSPORT_TYPE_SELECTOR = (By.CLASS_NAME, "types-container")
    CAR_TRANSPORT = (By.CSS_SELECTOR, ".type:not(.drive)")
    WALKING_TRANSPORT = (By.CSS_SELECTOR, ".type[class*='walking']")
    TAXI_TRANSPORT = (By.CSS_SELECTOR, ".type[class*='taxi']")
    BICYCLE_TRANSPORT = (By.CSS_SELECTOR, ".type[class*='bicycle']")
    SCOOTER_TRANSPORT = (By.CSS_SELECTOR, ".type[class*='scooter']")
    DRIVE_TRANSPORT = (By.CSS_SELECTOR, ".type.drive")
    ACTIVE_TRANSPORT = (By.CSS_SELECTOR, ".type.active")

    # Устаревшие локаторы для совместимости
    ROUTE_MODE_SELECTOR = (By.CLASS_NAME, "modes-container")
    WALKING_MODE = (By.XPATH, "//div[contains(@class, 'type') and contains(text(), 'walking')]")
    DRIVING_MODE = (By.XPATH, "//div[contains(@class, 'type') and contains(text(), 'car')]")
    TRANSIT_MODE = (By.XPATH, "//div[contains(@class, 'type') and contains(text(), 'transit')]")

    # Кнопки действий
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(), 'Забронировать')]")

    # Отображение результатов
    RESULTS_CONTAINER = (By.CLASS_NAME, "results-container")
    RESULTS_TEXT = (By.CLASS_NAME, "results-text")
    RESULTS_EXTRA = (By.CLASS_NAME, "results-extra")
    ROUTE_TYPE_TEXT = (By.CSS_SELECTOR, ".text")
    COST_TEXT = (By.CSS_SELECTOR, ".text")
