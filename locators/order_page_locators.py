"""Локаторы для страницы заказа."""

from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы элементов страницы заказа."""

    # Форма заказа
    ORDER_FORM = (By.CSS_SELECTOR, ".tariff-picker.shown")
    TARIFF_SELECTOR = (By.CLASS_NAME, "tariff-selector")
    ORDER_PRICE = (By.CLASS_NAME, "order-price")

    # Тарифы Такси (структура tcard с русским текстом)
    FARE_SELECTOR = (By.CLASS_NAME, "tariff-cards")
    BUSINESS_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Рабочий')]]")
    SLEEPY_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Сонный')]]")
    VACATION_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Отпускной')]]")
    TALKATIVE_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Разговорчивый')]]")
    COMFORTING_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Утешительный')]]")
    GLOSSY_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Глянцевый')]]")
    ACTIVE_FARE = (By.CSS_SELECTOR, ".tcard.active")
    ALL_FARES = (By.CSS_SELECTOR, ".tcard")

    # Всплывающие подсказки тарифов
    FARE_INFO_ICON = (By.CSS_SELECTOR, ".fare-info-icon, .info-icon")
    FARE_TOOLTIP = (By.CSS_SELECTOR, ".fare-tooltip, .tooltip")

    # Устаревшие локаторы тарифов для совместимости
    ECONOMY_TARIFF = (By.CSS_SELECTOR, "[data-tariff='economy']")
    COMFORT_TARIFF = (By.CSS_SELECTOR, "[data-tariff='comfort']")
    BUSINESS_TARIFF = (By.CSS_SELECTOR, "[data-tariff='business']")

    # Поля формы заказа
    PHONE_INPUT = (By.ID, "phone")
    PHONE_FIELD = (By.CSS_SELECTOR, "#phone, .phone-field, [data-field='phone']")
    PAYMENT_METHOD_SELECTOR = (By.CLASS_NAME, "payment-picker")
    PAYMENT_METHOD_FIELD = (By.CSS_SELECTOR, ".payment-picker, .payment-field, [data-field='payment']")
    COMMENT_INPUT = (By.ID, "comment")
    COMMENT_FIELD = (By.CSS_SELECTOR, "#comment, .comment-field, [data-field='comment']")
    REQUIREMENTS_FIELD = (By.CSS_SELECTOR, ".reqs")
    CARD_PAYMENT = (By.CSS_SELECTOR, "[data-payment='card']")
    CASH_PAYMENT = (By.CSS_SELECTOR, "[data-payment='cash']")

    # Требования к заказу (чекбоксы)
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".reqs-header")
    LAPTOP_TABLE_CHECKBOX = (By.CSS_SELECTOR, ".r-sw-container .switch-input")

    # Кнопки
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".confirm-order")
    ENTER_NUMBER_ORDER_BUTTON = (By.CSS_SELECTOR, "button.smart-button")
    SMART_BUTTON_MAIN = (By.CSS_SELECTOR, ".smart-button-main")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='order-btn-group' and .//div[text()='Отменить']]//button")
    DETAILS_BUTTON = (By.XPATH, "//div[@class='order-btn-group' and .//div[text()='Детали']]//button")
    ADD_LICENSE_BUTTON_NP = (By.CSS_SELECTOR, ".np-button")

    # Окно поиска машины
    CAR_SEARCH_WINDOW = (By.CSS_SELECTOR, ".order-body")
    CAR_SEARCH_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    CAR_SEARCH_TIMER = (By.CSS_SELECTOR, ".order-header-time")

    # Окно совершенного заказа
    COMPLETED_ORDER_WINDOW = (By.CSS_SELECTOR, ".order-body")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    FARE_IMAGE = (By.CSS_SELECTOR, ".order-number img[alt='Car']")

    # Информация о водителе
    DRIVER_INFO_BLOCK = (By.CSS_SELECTOR, ".order-btn-group .order-btn-rating")
    DRIVER_NAME = (By.CSS_SELECTOR, ".order-buttons .order-btn-group div:last-child")
    DRIVER_PHOTO = (By.CSS_SELECTOR, ".order-btn-group img[alt='close']")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")

    # Детали заказа
    ORDER_DETAILS_WINDOW = (By.CSS_SELECTOR, ".order-details")
    PICKUP_ADDRESS = (By.XPATH, "//div[contains(@class, 'order-details-row')]//div[contains(text(), 'Адрес подачи')]/preceding-sibling::div[@class='o-d-h']")
    DESTINATION_ADDRESS = (By.XPATH, "//div[contains(@class, 'order-details-row')]//div[contains(text(), 'Адрес назначения')]/preceding-sibling::div[@class='o-d-h']")
    PAYMENT_METHOD_DISPLAY = (By.XPATH, "//div[contains(@class, 'order-details-row')]//div[contains(text(), 'Способ оплаты')]/preceding-sibling::div[@class='o-d-h']")
    MORE_ABOUT_TRIP = (By.XPATH, "//div[contains(@class, 'order-details-row')]//div[contains(text(), 'Еще про поездку')]")
    TRIP_COST = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")

    # Заказ Драйв
    DRIVE_ORDER_FORM = (By.CSS_SELECTOR, ".tariff-picker.shown")
    TARIFF_CARDS = (By.CSS_SELECTOR, ".tariff-cards")
    EVERYDAY_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Повседневный')]]")
    OUTDOOR_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Походный')]]")
    LUXURY_FARE = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[contains(text(), 'Роскошный')]]")
    ACTIVE_TCARD = (By.CSS_SELECTOR, ".tcard.active")
    ALL_TCARDS = (By.CSS_SELECTOR, ".tcard")

    # Превью Драйв
    DRIVE_PREVIEW = (By.CSS_SELECTOR, ".drive-preview")
    DRIVE_PREVIEW_TITLE = (By.CSS_SELECTOR, ".drive-preview-title")
    DRIVE_PREVIEW_PREFIX = (By.CSS_SELECTOR, ".drive-preview-prefix")

    # Окно добавления прав (секция становится видимой при нажатии smart-button)
    LICENSE_WINDOW = (By.CSS_SELECTOR, ".section.active")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    DATE_OF_BIRTH_INPUT = (By.ID, "birthDate")
    LICENSE_NUMBER_INPUT = (By.ID, "number")
    # Кнопка Добавить в форме с полями ввода прав
    ADD_LICENSE_BUTTON = (By.XPATH, "//div[contains(@class, 'section') and contains(@class, 'active') and .//input[@id='firstName']]//button[contains(@class, 'button') and contains(@class, 'full')]")
    CANCEL_LICENSE_BUTTON = (By.CSS_SELECTOR, ".close-button.section-close")
    # Окно подтверждения после добавления прав (содержит текст "Спасибо")
    LICENSE_CONFIRMATION_WINDOW = (By.CSS_SELECTOR, ".section.active .head")
    LICENSE_CONFIRMATION_BUTTON = (By.XPATH, "//div[contains(@class, 'section') and contains(@class, 'active') and .//div[contains(@class, 'head')]]//button[contains(@class, 'button') and contains(@class, 'full')]")

    # Окно совершенного заказа Драйв
    DRIVE_ORDER_WINDOW = (By.CSS_SELECTOR, ".order-body")
    FREE_WAITING_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    FREE_WAITING_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    CAR_LOCATION_ADDRESS = (By.CSS_SELECTOR, ".o-d-h")

    # Локаторы для динамического поиска тарифов
    TCARD_BY_NAME_TEMPLATE = "//div[contains(@class, 'tcard')]//div[contains(text(), '{}')]"
    TCARD_PARENT_BY_NAME_TEMPLATE = "//div[contains(@class, 'tcard')]//div[contains(text(), '{}')]/ancestor::div[contains(@class, 'tcard')]"

    # Локаторы для всплывающих подсказок
    TAXI_TOOLTIP_TEXT = (By.CSS_SELECTOR, ".i-dPrefix")
    ACTIVE_TCARD_DESC = (By.CSS_SELECTOR, ".tcard.active .tcard-desc, .tcard.active .description")

    # Локатор для ожидания завершения поиска машины
    COMPLETED_ORDER_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'мин.') and contains(text(), 'приедет')]")
    SEARCHING_CAR_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'Поиск машины')]")

