"""
Page Object для главной страницы сервиса EZ Route.
"""
from base_object.base_object import BaseObject
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseObject):
    """Класс для работы с главной страницей маршрутизатора"""

    # Предустановленные адреса
    ADDRESS_HAMOVNICHESKY = "Хамовнический вал, 34"
    ADDRESS_ZUBOVSKY = "Зубовский бульвар, 37"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = MainPageLocators

    def enter_from_address(self, address: str) -> None:
        """
        Ввод адреса в поле "Откуда"

        :param address: адрес для ввода
        """
        self.clean_field(self.locators.FROM_FIELD)
        self.send_keys(self.locators.FROM_FIELD, address)

    def enter_to_address(self, address: str) -> None:
        """
        Ввод адреса в поле "Куда"

        :param address: адрес для ввода
        """
        self.clean_field(self.locators.TO_FIELD)
        self.send_keys(self.locators.TO_FIELD, address)

    def set_route(self, from_address: str, to_address: str) -> None:
        """
        Установка маршрута от одного адреса до другого

        :param from_address: адрес начала маршрута
        :param to_address: адрес конца маршрута
        """
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)

    def is_map_visible(self) -> bool:
        """
        Проверка видимости карты

        :return: True если карта видна
        """
        self._is_visible(self.locators.MAP_CONTAINER)
        return True

    def get_route_points_count(self) -> int:
        """
        Получение количества точек маршрута на карте

        :return: количество точек маршрута
        """
        return self.get_elements_count(self.locators.ROUTE_POINTS)

    def get_map_markers_count(self) -> int:
        """
        Получение количества маркеров на карте

        :return: количество маркеров
        """
        return self.get_elements_count(self.locators.MAP_MARKERS, min_count=1)

    def is_route_start_point_visible(self) -> bool:
        """
        Проверка видимости точки начала маршрута

        :return: True если точка начала видна
        """
        self._is_visible(self.locators.ROUTE_START_POINT)
        return True

    def is_route_end_point_visible(self) -> bool:
        """
        Проверка видимости точки конца маршрута

        :return: True если точка конца видна
        """
        self._is_visible(self.locators.ROUTE_END_POINT)
        return True

    def are_both_route_points_visible(self) -> bool:
        """
        Проверка видимости обеих точек маршрута (начала и конца)

        :return: True если обе точки видны
        """
        return self.is_route_start_point_visible() and self.is_route_end_point_visible()

    def is_route_line_visible(self) -> bool:
        """
        Проверка видимости линии маршрута

        :return: True если линия маршрута видна
        """
        self._is_visible(self.locators.ROUTE_LINE)
        return True

    def wait_for_route_to_display(self, timeout: int = 10) -> bool:
        """
        Ожидание отображения маршрута на карте

        :param timeout: время ожидания в секундах
        :return: True если маршрут отобразился
        """
        return self.wait_for_elements_count(self.locators.MAP_MARKERS, min_count=2, timeout=timeout)

    def is_route_selection_block_visible(self) -> bool:
        """
        Проверка видимости блока выбора маршрута

        :return: True если блок выбора маршрута видим
        """
        self._is_visible(self.locators.ROUTE_SELECTION_BLOCK)
        return True

    def get_route_selection_block_text(self) -> str:
        """
        Получение текста из блока выбора маршрута

        :return: текст блока выбора маршрута
        """
        element = self._is_visible(self.locators.ROUTE_SELECTION_BLOCK)
        return " ".join(element.text.split())

    def wait_for_route_selection_block(self, timeout: int = 10) -> bool:
        return self.wait_for_condition(
            EC.visibility_of_element_located(self.locators.ROUTE_SELECTION_BLOCK),
            timeout=timeout
        )

