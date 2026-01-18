"""Page Object для главной страницы с полями ввода адресов."""

import allure
from pages.base_object import BaseObject
from locators.main_page_locators import MainPageLocators


class MainPage(BaseObject):
    """Page Object для главной страницы с полями ввода адресов."""

    @allure.step("Ввод адреса отправления: {address}")
    def enter_from_address(self, address: str) -> None:
        """Ввод адреса отправления."""
        self.send_keys(MainPageLocators.FROM_INPUT, address)

    @allure.step("Ввод адреса назначения: {address}")
    def enter_to_address(self, address: str) -> None:
        """Ввод адреса назначения."""
        self.send_keys(MainPageLocators.TO_INPUT, address)

    @allure.step("Построение маршрута от '{from_address}' до '{to_address}'")
    def build_route(self, from_address: str, to_address: str) -> None:
        """Полный флоу построения маршрута."""
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)
        self.wait_for_route_to_be_built()

    @allure.step("Ожидание построения маршрута")
    def wait_for_route_to_be_built(self) -> None:
        """Ожидание завершения расчета маршрута."""
        self.wait_for_element_visible(MainPageLocators.ROUTE_INFO)

    @allure.step("Проверка отображения информации о маршруте")
    def is_route_info_displayed(self) -> bool:
        """Проверка видимости информации о маршруте."""
        return self.is_element_visible(MainPageLocators.ROUTE_INFO)

    @allure.step("Получение текста информации о маршруте")
    def get_route_info_text(self) -> str:
        """Получение текста из блока информации о маршруте."""
        return self.get_text(MainPageLocators.ROUTE_INFO)

    @allure.step("Проверка отображения кнопки 'Заказать такси'")
    def is_order_taxi_button_displayed(self) -> bool:
        """Проверка видимости кнопки заказа такси."""
        return self.is_element_visible(MainPageLocators.ORDER_TAXI_BUTTON)

    @allure.step("Клик по кнопке 'Заказать такси'")
    def click_order_taxi(self) -> None:
        """Клик по кнопке заказа такси."""
        self.click(MainPageLocators.ORDER_TAXI_BUTTON)

    @allure.step("Проверка отображения карты")
    def is_map_displayed(self) -> bool:
        """Проверка видимости контейнера карты."""
        return self.is_element_visible(MainPageLocators.MAP_CONTAINER)

    @allure.step("Получение значения поля 'Откуда'")
    def get_from_input_value(self) -> str:
        """Получение текущего значения поля 'Откуда'."""
        return self.get_attribute(MainPageLocators.FROM_INPUT, "value")

    @allure.step("Получение значения поля 'Куда'")
    def get_to_input_value(self) -> str:
        """Получение текущего значения поля 'Куда'."""
        return self.get_attribute(MainPageLocators.TO_INPUT, "value")

    @allure.step("Ожидание загрузки страницы через JavaScript")
    def wait_for_page_load(self) -> None:
        """Использование JavaScript для ожидания полной загрузки страницы."""
        self.execute_script(
            "return new Promise(resolve => setTimeout(resolve, 500));"
        )

    @allure.step("Наведение на контейнер карты")
    def hover_over_map(self) -> None:
        """Наведение на элемент карты."""
        self.hover(MainPageLocators.MAP_CONTAINER)

    @allure.step("Проверка отображения маркера начала маршрута")
    def is_start_marker_displayed(self) -> bool:
        """Проверка видимости маркера начальной точки на карте."""
        return self.is_element_visible(MainPageLocators.START_MARKER)

    @allure.step("Проверка отображения маркера конца маршрута")
    def is_end_marker_displayed(self) -> bool:
        """Проверка видимости маркера конечной точки на карте."""
        return self.is_element_visible(MainPageLocators.END_MARKER)

    @allure.step("Проверка отображения линии маршрута")
    def is_route_line_displayed(self) -> bool:
        """Проверка видимости линии маршрута на карте."""
        return self.is_element_visible(MainPageLocators.ROUTE_LINE)
