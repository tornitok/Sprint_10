"""Test data module containing addresses and other test constants."""


class Addresses:
    """Preset addresses available in the application."""

    FROM_ADDRESS = "Хамовнический Вал, 34"
    TO_ADDRESS = "Зубовский бульвар, 37"

    # Alternative English transliterations
    FROM_ADDRESS_EN = "Hamovnicheskij Val, 34"
    TO_ADDRESS_EN = "Zubovskij Boulevard, 37"


class RouteTypes:
    """Route type options."""

    OPTIMAL = "Optimal"
    FAST = "Fast"
    CUSTOM = "Custom"


class TransportTypes:
    """Transport type options for Custom route."""

    CAR = "Car"
    WALKING = "Walking"
    TAXI = "Taxi"
    BICYCLE = "Bicycle"
    SCOOTER = "Scooter"
    DRIVE = "Drive"


class TaxiFares:
    """Taxi fare options."""

    BUSINESS = "Business"
    SLEEPY = "Sleepy"
    VACATION = "Vacation"
    TALKATIVE = "Talkative"
    COMFORTING = "Comforting"
    GLOSSY = "Glossy"

    ALL_FARES = [BUSINESS, SLEEPY, VACATION, TALKATIVE, COMFORTING, GLOSSY]


class TaxiFareDescriptions:
    """Taxi fare descriptions for tooltips."""

    BUSINESS = "For focused professionals"
    SLEEPY = "For those who did not get enough sleep"
    VACATION = "When it is time to relax"
    TALKATIVE = "When thoughts need to be spoken"
    COMFORTING = "When you want emotional support"
    GLOSSY = "When you need to shine"

    DESCRIPTIONS = {
        TaxiFares.BUSINESS: BUSINESS,
        TaxiFares.SLEEPY: SLEEPY,
        TaxiFares.VACATION: VACATION,
        TaxiFares.TALKATIVE: TALKATIVE,
        TaxiFares.COMFORTING: COMFORTING,
        TaxiFares.GLOSSY: GLOSSY,
    }


class DriveFares:
    """Drive fare options."""

    EVERYDAY = "Everyday"
    OUTDOOR = "Outdoor"
    LUXURY = "Luxury"

    ALL_FARES = [EVERYDAY, OUTDOOR, LUXURY]


class DriveFareDescriptions:
    """Drive fare descriptions."""

    EVERYDAY = "BMW 750, simple daily trips"
    OUTDOOR = "KIA RIO, for traveling"
    LUXURY = "PORSCHE 911, shine and power"

    DESCRIPTIONS = {
        DriveFares.EVERYDAY: EVERYDAY,
        DriveFares.OUTDOOR: OUTDOOR,
        DriveFares.LUXURY: LUXURY,
    }


class ExpectedTexts:
    """Expected UI texts for assertions."""

    ROUTE_BUILT_MESSAGE = "Маршрут построен"
    ORDER_TAXI_BUTTON = "Заказать такси"
    CALL_TAXI_BUTTON = "Call Taxi"
    BOOK_BUTTON = "Book"
    SEARCHING_FOR_CAR = "Searching for a car"
    CAR_BOOKED = "Car booked"
    MINUTES_AND_ARRIVING = "minutes and arriving"
    CANCEL_BUTTON = "Cancel"
    DETAILS_BUTTON = "Details"
    ADD_BUTTON = "Add"
    ENTER_NUMBER_AND_ORDER = "Enter number and order"

    # Same address route text
    SAME_ADDRESS_ROUTE_TYPE = "Auto"
    SAME_ADDRESS_COST = "Free"
    SAME_ADDRESS_TRAVEL_TIME = "Travel time: 0 min"


class OrderFormFields:
    """Order form field labels."""

    PHONE_NUMBER = "Phone number"
    PAYMENT_METHOD = "Payment method"
    COMMENT_FOR_DRIVER = "Comment for driver"
    ORDER_REQUIREMENTS = "Order requirements"


class DriverLicenseFields:
    """Driver license form field labels."""

    FIRST_NAME = "First name"
    LAST_NAME = "Last name"
    DATE_OF_BIRTH = "Date of birth"
    LICENSE_NUMBER = "License number"


class Urls:
    """Application URLs."""

    BASE_URL = "https://ez-route.stand.praktikum-services.ru/"
