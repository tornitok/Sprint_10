"""Locators for the Order Page."""

from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Locators for Order Page elements."""

    # Order Form
    ORDER_FORM = (By.CLASS_NAME, "order-form")
    TARIFF_SELECTOR = (By.CLASS_NAME, "tariff-selector")
    ORDER_PRICE = (By.CLASS_NAME, "order-price")

    # Taxi Fares
    FARE_SELECTOR = (By.CLASS_NAME, "fare-selector")
    BUSINESS_FARE = (By.CSS_SELECTOR, "[data-fare='business']")
    SLEEPY_FARE = (By.CSS_SELECTOR, "[data-fare='sleepy']")
    VACATION_FARE = (By.CSS_SELECTOR, "[data-fare='vacation']")
    TALKATIVE_FARE = (By.CSS_SELECTOR, "[data-fare='talkative']")
    COMFORTING_FARE = (By.CSS_SELECTOR, "[data-fare='comforting']")
    GLOSSY_FARE = (By.CSS_SELECTOR, "[data-fare='glossy']")
    ACTIVE_FARE = (By.CSS_SELECTOR, ".fare-option.active, [data-fare].active")
    ALL_FARES = (By.CSS_SELECTOR, "[data-fare]")

    # Fare Info Tooltip
    FARE_INFO_ICON = (By.CSS_SELECTOR, ".fare-info-icon, .info-icon")
    FARE_TOOLTIP = (By.CSS_SELECTOR, ".fare-tooltip, .tooltip")

    # Legacy tariff locators for compatibility
    ECONOMY_TARIFF = (By.CSS_SELECTOR, "[data-tariff='economy']")
    COMFORT_TARIFF = (By.CSS_SELECTOR, "[data-tariff='comfort']")
    BUSINESS_TARIFF = (By.CSS_SELECTOR, "[data-tariff='business']")

    # Order Form Fields
    PHONE_INPUT = (By.ID, "phone")
    PHONE_FIELD = (By.CSS_SELECTOR, ".phone-field, [data-field='phone']")
    PAYMENT_METHOD_SELECTOR = (By.CLASS_NAME, "payment-method")
    PAYMENT_METHOD_FIELD = (By.CSS_SELECTOR, ".payment-field, [data-field='payment']")
    COMMENT_INPUT = (By.ID, "comment")
    COMMENT_FIELD = (By.CSS_SELECTOR, ".comment-field, [data-field='comment']")
    REQUIREMENTS_FIELD = (By.CSS_SELECTOR, ".requirements-field, [data-field='requirements']")
    CARD_PAYMENT = (By.CSS_SELECTOR, "[data-payment='card']")
    CASH_PAYMENT = (By.CSS_SELECTOR, "[data-payment='cash']")

    # Order Requirements (Checkboxes)
    LAPTOP_TABLE_CHECKBOX = (By.CSS_SELECTOR, "[data-requirement='laptop-table']")

    # Buttons
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".confirm-order")
    ENTER_NUMBER_ORDER_BUTTON = (By.CSS_SELECTOR, ".enter-number-order, [data-action='enter-number-order']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, ".cancel-button, [data-action='cancel']")
    DETAILS_BUTTON = (By.CSS_SELECTOR, ".details-button, [data-action='details']")

    # Car Search Window
    CAR_SEARCH_WINDOW = (By.CSS_SELECTOR, ".car-search-window, .search-modal")
    CAR_SEARCH_TITLE = (By.CSS_SELECTOR, ".car-search-title, .search-title")
    CAR_SEARCH_TIMER = (By.CSS_SELECTOR, ".search-timer, .countdown-timer")

    # Completed Order Window
    COMPLETED_ORDER_WINDOW = (By.CSS_SELECTOR, ".completed-order-window, .order-complete")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order-title")
    CAR_NUMBER = (By.CSS_SELECTOR, ".car-number")
    FARE_IMAGE = (By.CSS_SELECTOR, ".fare-image")

    # Driver Info
    DRIVER_INFO_BLOCK = (By.CSS_SELECTOR, ".driver-info")
    DRIVER_NAME = (By.CSS_SELECTOR, ".driver-name")
    DRIVER_PHOTO = (By.CSS_SELECTOR, ".driver-photo")
    DRIVER_RATING = (By.CSS_SELECTOR, ".driver-rating")

    # Order Details
    ORDER_DETAILS_WINDOW = (By.CSS_SELECTOR, ".order-details-window, .details-modal")
    PICKUP_ADDRESS = (By.CSS_SELECTOR, ".pickup-address, .from-address")
    DESTINATION_ADDRESS = (By.CSS_SELECTOR, ".destination-address, .to-address")
    PAYMENT_METHOD_DISPLAY = (By.CSS_SELECTOR, ".payment-method-display")
    MORE_ABOUT_TRIP = (By.CSS_SELECTOR, ".more-about-trip")
    TRIP_COST = (By.CSS_SELECTOR, ".trip-cost, .order-cost")

    # Drive Order
    DRIVE_ORDER_FORM = (By.CSS_SELECTOR, ".drive-order-form")
    EVERYDAY_FARE = (By.CSS_SELECTOR, "[data-drive-fare='everyday']")
    OUTDOOR_FARE = (By.CSS_SELECTOR, "[data-drive-fare='outdoor']")
    LUXURY_FARE = (By.CSS_SELECTOR, "[data-drive-fare='luxury']")

    # Driver License Window
    LICENSE_WINDOW = (By.CSS_SELECTOR, ".license-window, .add-license-modal")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-field='first-name'], #first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-field='last-name'], #last-name")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "[data-field='date-of-birth'], #date-of-birth")
    LICENSE_NUMBER_INPUT = (By.CSS_SELECTOR, "[data-field='license-number'], #license-number")
    ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, ".add-license-button, [data-action='add-license']")
    CANCEL_LICENSE_BUTTON = (By.CSS_SELECTOR, ".cancel-license-button")

    # Completed Drive Order Window
    DRIVE_ORDER_WINDOW = (By.CSS_SELECTOR, ".drive-order-complete")
    FREE_WAITING_TIMER = (By.CSS_SELECTOR, ".free-waiting-timer")
    CAR_LOCATION_ADDRESS = (By.CSS_SELECTOR, ".car-location-address")
