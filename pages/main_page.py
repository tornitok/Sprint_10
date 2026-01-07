"""
Page Object для главной страницы сервиса EZ Route.
"""
from base_object.base_object import BaseObject
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseObject):
    ADDRESS_HAMOVNICHESKY = "Хамовнический вал, 34"
    ADDRESS_ZUBOVSKY = "Зубовский бульвар, 37"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = MainPageLocators

    def enter_from_address(self, address: str) -> None:
        self.clean_field(self.locators.FROM_FIELD)
        self.send_keys(self.locators.FROM_FIELD, address)

    def enter_to_address(self, address: str) -> None:
        self.clean_field(self.locators.TO_FIELD)
        self.send_keys(self.locators.TO_FIELD, address)

    def set_route(self, from_address: str, to_address: str) -> None:
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)

    def is_map_visible(self) -> bool:
        self._is_visible(self.locators.MAP_CONTAINER)
        return True

    def get_route_points_count(self) -> int:
        return self.get_elements_count(self.locators.ROUTE_POINTS)

    def get_map_markers_count(self) -> int:
        return self.get_elements_count(self.locators.MAP_MARKERS, min_count=1)

    def is_route_start_point_visible(self) -> bool:
        self._is_visible(self.locators.ROUTE_START_POINT)
        return True

    def is_route_end_point_visible(self) -> bool:
        self._is_visible(self.locators.ROUTE_END_POINT)
        return True

    def are_both_route_points_visible(self) -> bool:
        return self.is_route_start_point_visible() and self.is_route_end_point_visible()

    def is_route_line_visible(self) -> bool:
        self._is_visible(self.locators.ROUTE_LINE)
        return True

    def wait_for_route_to_display(self, timeout: int = 10) -> bool:
        return self.wait_for_elements_count(self.locators.MAP_MARKERS, min_count=2, timeout=timeout)

    def is_route_selection_block_visible(self) -> bool:
        self._is_visible(self.locators.ROUTE_SELECTION_BLOCK)
        return True

    def get_route_selection_block_text(self) -> str:
        element = self._is_visible(self.locators.ROUTE_SELECTION_BLOCK)
        return " ".join(element.text.split())

    def wait_for_route_selection_block(self, timeout: int = 10) -> bool:
        return self.wait_for_condition(
            EC.visibility_of_element_located(self.locators.ROUTE_SELECTION_BLOCK),
            timeout=timeout
        )

    def click_route_type_optimal(self) -> None:
        """Выбор вида маршрута Оптимальный"""
        self.click(self.locators.ROUTE_TYPE_OPTIMAL)

    def click_route_type_fast(self) -> None:
        """Выбор вида маршрута Быстрый"""
        self.click(self.locators.ROUTE_TYPE_FAST)

    def click_route_type_custom(self) -> None:
        """Выбор вида маршрута Свой"""
        self.click(self.locators.ROUTE_TYPE_CUSTOM)

    def get_active_route_type(self) -> str:
        """Получение текста активного вида маршрута"""
        return self.get_text(self.locators.ACTIVE_ROUTE_TYPE)

    # Методы для работы с типами передвижения
    def click_transport_type_taxi(self) -> None:
        """Выбор типа передвижения Такси"""
        self.click(self.locators.TRANSPORT_TYPE_TAXI)

    def click_transport_type_drive(self) -> None:
        """Выбор типа передвижения Драйв"""
        self.click(self.locators.TRANSPORT_TYPE_DRIVE)

    def get_active_transport_type(self) -> str:
        """Получение текста активного типа передвижения"""
        return self.get_text(self.locators.ACTIVE_TRANSPORT_TYPE)

    def get_transport_types_count(self) -> int:
        """Получение количества доступных типов передвижения"""
        return self.get_elements_count(self.locators.TRANSPORT_TYPES)

    def are_transport_types_visible(self) -> bool:
        """Проверка видимости типов передвижения"""
        self._is_visible(self.locators.TRANSPORT_TYPES)
        return True

    # Методы для работы с информацией о маршруте
    def get_route_cost(self) -> str:
        """Получение стоимости маршрута"""
        return self.get_text(self.locators.ROUTE_COST)

    def get_route_time(self) -> str:
        """Получение времени в пути"""
        return self.get_text(self.locators.ROUTE_TIME)

    # Методы для кнопок
    def is_call_taxi_button_active(self) -> bool:
        """Проверка активности кнопки Вызвать такси"""
        element = self._is_visible(self.locators.CALL_TAXI_BUTTON)
        return element.is_enabled()

    def click_call_taxi_button(self) -> None:
        """Нажатие кнопки Вызвать такси"""
        self.click(self.locators.CALL_TAXI_BUTTON)

    def is_book_button_active(self) -> bool:
        """Проверка активности кнопки Забронировать"""
        element = self._is_visible(self.locators.BOOK_BUTTON)
        return element.is_enabled()

    # Методы для работы с формой заказа такси
    def is_taxi_order_form_visible(self) -> bool:
        """Проверка видимости формы заказа такси"""
        self._is_visible(self.locators.TAXI_ORDER_FORM)
        return True

    def get_taxi_tariffs_count(self) -> int:
        """Получение количества тарифов такси"""
        return self.get_elements_count(self.locators.TAXI_TARIFFS)

    def is_tariff_active(self) -> bool:
        """Проверка наличия активного тарифа"""
        self._is_visible(self.locators.ACTIVE_TARIFF)
        return True

    def click_taxi_tariff_working(self) -> None:
        """Выбор тарифа Рабочий"""
        self.click(self.locators.TAXI_TARIFF_WORKING)

    def get_tariff_description(self) -> str:
        """Получение описания тарифа из всплывающего окна"""
        return self.get_text(self.locators.TARIFF_DESCRIPTION_POPUP)

    def click_laptop_table_checkbox(self) -> None:
        """Включение чекбокса Столик для ноутбука"""
        self.click(self.locators.LAPTOP_TABLE_CHECKBOX)

    def click_enter_number_and_order_button(self) -> None:
        """Нажатие кнопки Ввести номер и заказать"""
        self.click(self.locators.ENTER_NUMBER_AND_ORDER_BUTTON)

    # Методы для окна ожидания
    def is_waiting_window_visible(self) -> bool:
        """Проверка видимости окна ожидания машины"""
        self._is_visible(self.locators.WAITING_WINDOW)
        return True

    def is_waiting_title_visible(self) -> bool:
        """Проверка видимости заголовка Поиск машины"""
        self._is_visible(self.locators.WAITING_TITLE)
        return True

    def is_waiting_timer_visible(self) -> bool:
        """Проверка видимости таймера"""
        self._is_visible(self.locators.WAITING_TIMER)
        return True

    def click_cancel_button(self) -> None:
        """Нажатие кнопки Отменить"""
        self.click(self.locators.CANCEL_BUTTON)

    def click_details_button(self) -> None:
        """Нажатие кнопки Детали"""
        self.click(self.locators.DETAILS_BUTTON)

    def wait_for_timer_complete(self, timeout: int = 60) -> bool:
        """Ожидание завершения таймера поиска машины"""
        return self.wait_for_condition(
            EC.invisibility_of_element_located(self.locators.WAITING_TIMER),
            timeout=timeout
        )

    # Методы для окна деталей
    def is_details_window_visible(self) -> bool:
        """Проверка видимости окна деталей"""
        self._is_visible(self.locators.DETAILS_WINDOW)
        return True

    def get_trip_cost_from_details(self) -> str:
        """Получение стоимости поездки из окна деталей"""
        return self.get_text(self.locators.TRIP_COST)

    # Методы для окна совершенного заказа
    def is_order_complete_window_visible(self) -> bool:
        """Проверка видимости окна совершенного заказа"""
        self._is_visible(self.locators.ORDER_COMPLETE_WINDOW)
        return True

    def is_order_complete_title_visible(self) -> bool:
        """Проверка видимости заголовка с временем прибытия"""
        self._is_visible(self.locators.ORDER_COMPLETE_TITLE)
        return True

    def is_car_number_visible(self) -> bool:
        """Проверка видимости номера автомобиля"""
        self._is_visible(self.locators.CAR_NUMBER)
        return True

    def is_driver_info_visible(self) -> bool:
        """Проверка видимости информации о водителе"""
        self._is_visible(self.locators.DRIVER_NAME)
        self._is_visible(self.locators.DRIVER_PHOTO)
        self._is_visible(self.locators.DRIVER_RATING)
        return True

