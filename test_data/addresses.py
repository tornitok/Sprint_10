"""Test data module containing addresses and other test constants."""


class Addresses:
    """Preset addresses available in the application."""

    FROM_ADDRESS = "Хамовнический Вал, 34"
    TO_ADDRESS = "Зубовский бульвар, 37"

    # Alternative English transliterations
    FROM_ADDRESS_EN = "Hamovnicheskij Val, 34"
    TO_ADDRESS_EN = "Zubovskij Boulevard, 37"


class ExpectedTexts:
    """Expected UI texts for assertions."""

    ROUTE_BUILT_MESSAGE = "Маршрут построен"
    ORDER_TAXI_BUTTON = "Заказать такси"


class Urls:
    """Application URLs."""

    BASE_URL = "https://ez-route.stand.praktikum-services.ru/"
