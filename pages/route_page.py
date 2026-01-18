"""Page Object для страницы маршрута с опциями маршрута."""

import allure
from pages.base_object import BaseObject
from locators.route_page_locators import RoutePageLocators


class RoutePage(BaseObject):
    """Page Object для страницы маршрута с опциями маршрута."""

    @allure.step("Проверка отображения блока выбора маршрута")
    def is_route_options_displayed(self) -> bool:
        """Проверка видимости блока выбора маршрута."""
        return self.is_element_visible(RoutePageLocators.ROUTE_OPTIONS_BLOCK)

    @allure.step("Получение расстояния маршрута")
    def get_route_distance(self) -> str:
        """Получение отображаемого расстояния маршрута."""
        return self.get_text(RoutePageLocators.ROUTE_DISTANCE)

    @allure.step("Получение времени в пути")
    def get_route_duration(self) -> str:
        """Получение отображаемого времени маршрута."""
        return self.get_text(RoutePageLocators.ROUTE_DURATION)

    @allure.step("Выбор режима Пешком")
    def select_walking_mode(self) -> None:
        """Выбор пешего режима маршрута."""
        self.click(RoutePageLocators.WALKING_MODE)

    @allure.step("Выбор режима На машине")
    def select_driving_mode(self) -> None:
        """Выбор режима маршрута на машине."""
        self.click(RoutePageLocators.DRIVING_MODE)

    @allure.step("Выбор режима Транспорт")
    def select_transit_mode(self) -> None:
        """Выбор режима общественного транспорта."""
        self.click(RoutePageLocators.TRANSIT_MODE)

    @allure.step("Наведение на блок выбора маршрута")
    def hover_over_route_options(self) -> None:
        """Наведение на блок выбора маршрута."""
        self.hover(RoutePageLocators.ROUTE_OPTIONS_BLOCK)

    # Методы работы с видами маршрута
    @allure.step("Выбор маршрута Оптимальный")
    def select_optimal_route(self) -> None:
        """Выбор вида маршрута Оптимальный."""
        self.click(RoutePageLocators.OPTIMAL_TAB)

    @allure.step("Выбор маршрута Быстрый")
    def select_fast_route(self) -> None:
        """Выбор вида маршрута Быстрый."""
        self.click(RoutePageLocators.FAST_TAB)

    @allure.step("Выбор маршрута Свой")
    def select_custom_route(self) -> None:
        """Выбор вида маршрута Свой."""
        self.click(RoutePageLocators.CUSTOM_TAB)

    @allure.step("Получение текста активного таба маршрута")
    def get_active_route_tab_text(self) -> str:
        """Получение текста текущего активного таба маршрута."""
        return self.get_text(RoutePageLocators.ACTIVE_ROUTE_TAB)

    @allure.step("Проверка активности таба Оптимальный")
    def is_optimal_tab_active(self) -> bool:
        """Проверка активности таба Оптимальный."""
        element = self.find_element(RoutePageLocators.OPTIMAL_TAB)
        return "active" in element.get_attribute("class")

    @allure.step("Проверка активности таба Быстрый")
    def is_fast_tab_active(self) -> bool:
        """Проверка активности таба Быстрый."""
        element = self.find_element(RoutePageLocators.FAST_TAB)
        return "active" in element.get_attribute("class")

    @allure.step("Проверка активности таба Свой")
    def is_custom_tab_active(self) -> bool:
        """Проверка активности таба Свой."""
        element = self.find_element(RoutePageLocators.CUSTOM_TAB)
        return "active" in element.get_attribute("class")

    # Методы работы с типами передвижения
    @allure.step("Выбор типа передвижения Машина")
    def select_car_transport(self) -> None:
        """Выбор типа передвижения Машина."""
        self.click(RoutePageLocators.CAR_TRANSPORT)

    @allure.step("Выбор типа передвижения Пешком")
    def select_walking_transport(self) -> None:
        """Выбор типа передвижения Пешком."""
        self.click(RoutePageLocators.WALKING_TRANSPORT)

    @allure.step("Выбор типа передвижения Такси")
    def select_taxi_transport(self) -> None:
        """Выбор типа передвижения Такси."""
        self.click(RoutePageLocators.TAXI_TRANSPORT)

    @allure.step("Выбор типа передвижения Велосипед")
    def select_bicycle_transport(self) -> None:
        """Выбор типа передвижения Велосипед."""
        self.click(RoutePageLocators.BICYCLE_TRANSPORT)

    @allure.step("Выбор типа передвижения Самокат")
    def select_scooter_transport(self) -> None:
        """Выбор типа передвижения Самокат."""
        self.click(RoutePageLocators.SCOOTER_TRANSPORT)

    @allure.step("Выбор типа передвижения Драйв")
    def select_drive_transport(self) -> None:
        """Выбор типа передвижения Драйв."""
        self.click(RoutePageLocators.DRIVE_TRANSPORT)

    @allure.step("Проверка отображения селектора типов передвижения")
    def is_transport_selector_displayed(self) -> bool:
        """Проверка видимости селектора типов передвижения."""
        return self.is_element_visible(RoutePageLocators.TRANSPORT_TYPE_SELECTOR)

    @allure.step("Проверка видимости типа Машина")
    def is_car_transport_active(self) -> bool:
        """Проверка видимости типа передвижения Машина."""
        return self.is_element_visible(RoutePageLocators.CAR_TRANSPORT)

    @allure.step("Проверка видимости типа Пешком")
    def is_walking_transport_visible(self) -> bool:
        """Проверка видимости типа передвижения Пешком."""
        return self.is_element_visible(RoutePageLocators.WALKING_TRANSPORT)

    @allure.step("Проверка видимости типа Такси")
    def is_taxi_transport_visible(self) -> bool:
        """Проверка видимости типа передвижения Такси."""
        return self.is_element_visible(RoutePageLocators.TAXI_TRANSPORT)

    @allure.step("Проверка видимости типа Велосипед")
    def is_bicycle_transport_visible(self) -> bool:
        """Проверка видимости типа передвижения Велосипед."""
        return self.is_element_visible(RoutePageLocators.BICYCLE_TRANSPORT)

    @allure.step("Проверка видимости типа Самокат")
    def is_scooter_transport_visible(self) -> bool:
        """Проверка видимости типа передвижения Самокат."""
        return self.is_element_visible(RoutePageLocators.SCOOTER_TRANSPORT)

    @allure.step("Проверка видимости типа Драйв")
    def is_drive_transport_visible(self) -> bool:
        """Проверка видимости типа передвижения Драйв."""
        return self.is_element_visible(RoutePageLocators.DRIVE_TRANSPORT)

    # Методы работы с кнопками
    @allure.step("Проверка отображения кнопки Вызвать такси")
    def is_call_taxi_button_displayed(self) -> bool:
        """Проверка видимости кнопки Вызвать такси."""
        return self.is_element_visible(RoutePageLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверка активности кнопки Вызвать такси")
    def is_call_taxi_button_enabled(self) -> bool:
        """Проверка активности кнопки Вызвать такси."""
        element = self.find_element(RoutePageLocators.CALL_TAXI_BUTTON)
        return element.is_enabled()

    @allure.step("Клик по кнопке Вызвать такси")
    def click_call_taxi(self) -> None:
        """Клик по кнопке Вызвать такси."""
        self.click(RoutePageLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверка отображения кнопки Забронировать")
    def is_book_button_displayed(self) -> bool:
        """Проверка видимости кнопки Забронировать."""
        return self.is_element_visible(RoutePageLocators.BOOK_BUTTON)

    @allure.step("Проверка активности кнопки Забронировать")
    def is_book_button_enabled(self) -> bool:
        """Проверка активности кнопки Забронировать."""
        element = self.find_element(RoutePageLocators.BOOK_BUTTON)
        return element.is_enabled()

    @allure.step("Клик по кнопке Забронировать")
    def click_book(self) -> None:
        """Клик по кнопке Забронировать."""
        self.click(RoutePageLocators.BOOK_BUTTON)

    # Методы получения стоимости и времени
    @allure.step("Получение стоимости маршрута")
    def get_route_cost(self) -> str:
        """Получение отображаемой стоимости маршрута."""
        return self.get_text(RoutePageLocators.ROUTE_COST)

    @allure.step("Получение времени в пути")
    def get_route_travel_time(self) -> str:
        """Получение отображаемого времени в пути."""
        return self.get_text(RoutePageLocators.ROUTE_TRAVEL_TIME)

    @allure.step("Получение текста типа маршрута")
    def get_route_type_text(self) -> str:
        """Получение текста типа маршрута."""
        return self.get_text(RoutePageLocators.ROUTE_TYPE_TEXT)

    @allure.step("Получение текста стоимости")
    def get_cost_text(self) -> str:
        """Получение текста стоимости."""
        return self.get_text(RoutePageLocators.COST_TEXT)
