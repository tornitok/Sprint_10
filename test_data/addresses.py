"""Модуль тестовых данных с адресами и константами."""


class Addresses:
    """Предустановленные адреса приложения.

    Согласно спецификации:
    - Хамовнический вал, 34
    - Зубовский бульвар, 37
    """

    FROM_ADDRESS = "Хамовнический вал, 34"
    TO_ADDRESS = "Зубовский бульвар, 37"


class RouteTypes:
    """Виды маршрутов."""

    OPTIMAL = "Оптимальный"
    FAST = "Быстрый"
    CUSTOM = "Свой"


class TransportTypes:
    """Типы передвижения для маршрута Свой."""

    CAR = "Машина"
    WALKING = "Пешком"
    TAXI = "Такси"
    BICYCLE = "Велосипед"
    SCOOTER = "Самокат"
    DRIVE = "Драйв"


class TaxiFares:
    """Тарифы такси."""

    BUSINESS = "Рабочий"
    SLEEPY = "Сонный"
    VACATION = "Отпускной"
    TALKATIVE = "Разговорчивый"
    COMFORTING = "Утешительный"
    GLOSSY = "Глянцевый"

    ALL_FARES = [BUSINESS, SLEEPY, VACATION, TALKATIVE, COMFORTING, GLOSSY]
    FARES_COUNT = 6


class TaxiFareDescriptions:
    """Описания тарифов такси для всплывающих подсказок (русский UI).

    Согласно спецификации:
    - Рабочий - Для деловых особ, которых отвлекают
    - Сонный - Для тех, кто не выспался
    - Отпускной - Если пришла пора отдохнуть
    - Разговорчивый - Если мысли не выходят из головы
    - Утешительный - Если хочется свернуться калачиком
    - Глянцевый - Если нужно блистать
    """

    BUSINESS = "Для деловых особ, которых отвлекают"    # Рабочий
    SLEEPY = "Для тех, кто не выспался"                 # Сонный
    VACATION = "Если пришла пора отдохнуть"             # Отпускной
    TALKATIVE = "Если мысли не выходят из головы"       # Разговорчивый
    COMFORTING = "Если хочется свернуться калачиком"    # Утешительный
    GLOSSY = "Если нужно блистать"                      # Глянцевый

    DESCRIPTIONS = {
        TaxiFares.BUSINESS: BUSINESS,
        TaxiFares.SLEEPY: SLEEPY,
        TaxiFares.VACATION: VACATION,
        TaxiFares.TALKATIVE: TALKATIVE,
        TaxiFares.COMFORTING: COMFORTING,
        TaxiFares.GLOSSY: GLOSSY,
    }


class DriveFares:
    """Тарифы Драйв."""

    EVERYDAY = "Повседневный"
    OUTDOOR = "Походный"
    LUXURY = "Роскошный"

    ALL_FARES = [EVERYDAY, OUTDOOR, LUXURY]


class DriveFareDescriptions:
    """Описания тарифов Драйв (как показано в секции превью).

    Согласно спецификации:
    - Повседневный - BMW 750 Просто по делам, ничего лишнего
    - Походный - KIA RIO Для путешествий
    - Роскошный - PORSCHE 911 Блеск, мощь, глянец
    """

    # Описания на русском языке с сайта
    EVERYDAY = "Просто по делам, ничего лишнего"
    OUTDOOR = "Для путешествий"
    LUXURY = "Блеск, мощь, глянец"

    # Модели машин
    EVERYDAY_CAR = "BMW 750"
    OUTDOOR_CAR = "Kia Rio"
    LUXURY_CAR = "Porsche 911"

    DESCRIPTIONS = {
        DriveFares.EVERYDAY: EVERYDAY,
        DriveFares.OUTDOOR: OUTDOOR,
        DriveFares.LUXURY: LUXURY,
    }


class ExpectedTexts:
    """Ожидаемые тексты UI для проверок."""

    # Сообщения о маршруте
    ROUTE_BUILT_MESSAGE = "Маршрут построен"

    # Кнопки
    ORDER_TAXI_BUTTON = "Заказать такси"
    CALL_TAXI_BUTTON = "Вызвать такси"
    BOOK_BUTTON = "Забронировать"
    CANCEL_BUTTON = "Отменить"
    DETAILS_BUTTON = "Детали"
    ADD_BUTTON = "Добавить"
    ENTER_NUMBER_AND_ORDER = "Ввести номер и заказать"
    ENTER_LICENSE_AND_BOOK = "Ввести права и забронировать"

    # Окно поиска машины
    SEARCHING_FOR_CAR = "Поиск машины"

    # Окно совершенного заказа такси
    MINUTES_AND_ARRIVING = "мин. и приедет"

    # Окно совершенного заказа Драйв
    CAR_BOOKED = "Машина забронирована"
    FREE_WAITING = "Бесплатное ожидание"

    # Текст маршрута для одинаковых адресов (русский UI)
    SAME_ADDRESS_ROUTE_TYPE = "Авто"
    SAME_ADDRESS_COST = "Бесплатно"
    SAME_ADDRESS_TRAVEL_TIME = "В пути 0 мин."


class OrderFormFields:
    """Названия полей формы заказа."""

    PHONE_NUMBER = "Телефон"
    PAYMENT_METHOD = "Способ оплаты"
    COMMENT_FOR_DRIVER = "Комментарий водителю"
    ORDER_REQUIREMENTS = "Требования к заказу"


class DriverLicenseFields:
    """Названия полей формы добавления прав."""

    FIRST_NAME = "Имя"
    LAST_NAME = "Фамилия"
    DATE_OF_BIRTH = "Дата рождения"
    LICENSE_NUMBER = "Номер"


class Urls:
    """URL-адреса приложения."""

    BASE_URL = "https://ez-route.stand.praktikum-services.ru/"
