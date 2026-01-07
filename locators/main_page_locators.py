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

    # Виды маршрута
    ROUTE_TYPE_OPTIMAL = (By.XPATH, "//div[@class='route-type' and text()='Оптимальный']")
    ROUTE_TYPE_FAST = (By.XPATH, "//div[@class='route-type' and text()='Быстрый']")
    ROUTE_TYPE_CUSTOM = (By.XPATH, "//div[@class='route-type' and text()='Свой']")
    ACTIVE_ROUTE_TYPE = (By.XPATH, "//div[@class='route-type active']")

    # Типы передвижения
    TRANSPORT_TYPE_CAR = (By.XPATH, "//div[@class='transport-type' and text()='Машина']")
    TRANSPORT_TYPE_WALK = (By.XPATH, "//div[@class='transport-type' and text()='Пешком']")
    TRANSPORT_TYPE_TAXI = (By.XPATH, "//div[@class='transport-type' and text()='Такси']")
    TRANSPORT_TYPE_BIKE = (By.XPATH, "//div[@class='transport-type' and text()='Велосипед']")
    TRANSPORT_TYPE_SCOOTER = (By.XPATH, "//div[@class='transport-type' and text()='Самокат']")
    TRANSPORT_TYPE_DRIVE = (By.XPATH, "//div[@class='transport-type' and text()='Драйв']")
    ACTIVE_TRANSPORT_TYPE = (By.XPATH, "//div[@class='transport-type active']")
    TRANSPORT_TYPES = (By.CSS_SELECTOR, ".transport-type")

    # Информация о маршруте
    ROUTE_COST = (By.CSS_SELECTOR, ".route-cost, [class*='cost']")
    ROUTE_TIME = (By.CSS_SELECTOR, ".route-time, [class*='time']")

    # Кнопки
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(), 'Забронировать')]")

    # Форма заказа такси
    TAXI_ORDER_FORM = (By.CSS_SELECTOR, ".taxi-order-form, [class*='taxi-order']")

    # Тарифы такси
    TAXI_TARIFF_WORKING = (By.XPATH, "//div[@class='tariff' and contains(., 'Рабочий')]")
    TAXI_TARIFF_SLEEPY = (By.XPATH, "//div[@class='tariff' and contains(., 'Сонный')]")
    TAXI_TARIFF_VACATION = (By.XPATH, "//div[@class='tariff' and contains(., 'Отпускной')]")
    TAXI_TARIFF_TALKATIVE = (By.XPATH, "//div[@class='tariff' and contains(., 'Разговорчивый')]")
    TAXI_TARIFF_COMFORTING = (By.XPATH, "//div[@class='tariff' and contains(., 'Утешительный')]")
    TAXI_TARIFF_GLOSSY = (By.XPATH, "//div[@class='tariff' and contains(., 'Глянцевый')]")
    TAXI_TARIFFS = (By.CSS_SELECTOR, ".tariff")
    ACTIVE_TARIFF = (By.CSS_SELECTOR, ".tariff.active")

    # Иконки описания тарифов
    TARIFF_INFO_ICON = (By.CSS_SELECTOR, ".tariff .info-icon, .tariff i")
    TARIFF_DESCRIPTION_POPUP = (By.CSS_SELECTOR, ".tariff-description, .tooltip")

    # Поля формы такси
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='phone'], #phone")
    PAYMENT_METHOD_FIELD = (By.CSS_SELECTOR, "input[name='payment'], #payment")
    DRIVER_COMMENT_FIELD = (By.CSS_SELECTOR, "textarea[name='comment'], #comment")
    ORDER_REQUIREMENTS_FIELD = (By.CSS_SELECTOR, "textarea[name='requirements'], #requirements")

    # Чекбоксы требований
    LAPTOP_TABLE_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and contains(@name, 'laptop')]")

    # Кнопка заказа такси
    ENTER_NUMBER_AND_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Ввести номер и заказать')]")

    # Окно ожидания машины
    WAITING_WINDOW = (By.CSS_SELECTOR, ".waiting-window, [class*='waiting']")
    WAITING_TITLE = (By.XPATH, "//h2[text()='Поиск машины']")
    WAITING_TIMER = (By.CSS_SELECTOR, ".timer, [class*='timer']")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отменить')]")
    DETAILS_BUTTON = (By.XPATH, "//button[contains(text(), 'Детали')]")

    # Окно деталей заказа
    DETAILS_WINDOW = (By.CSS_SELECTOR, ".details-window, [class*='details']")
    PICKUP_ADDRESS = (By.CSS_SELECTOR, ".pickup-address, [class*='pickup']")
    DESTINATION_ADDRESS = (By.CSS_SELECTOR, ".destination-address, [class*='destination']")
    PAYMENT_METHOD_INFO = (By.CSS_SELECTOR, ".payment-method, [class*='payment']")
    TRIP_COST = (By.CSS_SELECTOR, ".trip-cost, [class*='cost']")

    # Окно совершенного заказа такси
    ORDER_COMPLETE_WINDOW = (By.CSS_SELECTOR, ".order-complete, [class*='complete']")
    ORDER_COMPLETE_TITLE = (By.XPATH, "//*[contains(text(), 'мин. и приедет')]")
    CAR_NUMBER = (By.CSS_SELECTOR, ".car-number, [class*='car-number']")
    TARIFF_IMAGE = (By.CSS_SELECTOR, ".tariff-image, [class*='tariff-img']")
    DRIVER_NAME = (By.CSS_SELECTOR, ".driver-name, [class*='driver-name']")
    DRIVER_PHOTO = (By.CSS_SELECTOR, ".driver-photo, [class*='driver-photo']")
    DRIVER_RATING = (By.CSS_SELECTOR, ".driver-rating, [class*='rating']")
