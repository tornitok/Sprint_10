"""Тесты на функциональность 'Заказ Драйв'."""

import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import (
    Addresses,
    DriveFares,
    DriveFareDescriptions,
)


@allure.feature("Заказ Драйв")
@allure.story("Функциональность заказа Драйв")
class TestDriveOrder:
    """Класс тестов для функциональности заказа Драйв.

    Блок заказа Драйв - Техническая спецификация
    Предусловия:
    - Ввести два разных предустановленных адреса
    - Выбрать маршрут Свой
    - Выбрать тип передвижения Драйв
    - Нажать кнопку Забронировать
    """

    def _navigate_to_drive_order(self, driver):
        """Вспомогательный метод для перехода к форме заказа Драйв."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        return main_page, route_page, OrderPage(driver)

    @allure.title("Проверка открытия формы заказа Драйв после нажатия Забронировать")
    @allure.description(
        "Проверка открытия формы заказа Драйв после нажатия кнопки Забронировать"
    )
    def test_drive_order_form_opens(self, open_main_page):
        """Тест отображения формы заказа Драйв."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Проверить отображение формы заказа Драйв"):
            assert order_page.is_drive_order_form_displayed(), (
                "Форма заказа Драйв должна отображаться после нажатия Забронировать"
            )

    @allure.title("Проверка наличия всех тарифов Драйв")
    @allure.description(
        "Проверка отображения всех тарифов Драйв: Повседневный, Походный, Роскошный"
    )
    def test_all_drive_fares_present(self, open_main_page):
        """Тест доступности всех тарифов Драйв."""
        _, _, order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Проверить видимость всех тарифов Драйв"):
            missing_fares = []
            for fare in DriveFares.ALL_FARES:
                if not order_page.is_fare_visible(fare.lower()):
                    missing_fares.append(fare)

            assert not missing_fares, (
                f"Отсутствующие тарифы Драйв: {missing_fares}. "
                f"Ожидались все: {DriveFares.ALL_FARES}"
            )


@allure.feature("Заказ Драйв")
@allure.story("Описания тарифов Драйв")
class TestDriveFareDescriptions:
    """Класс тестов для всплывающих подсказок описания тарифов Драйв."""

    def _navigate_to_drive_order(self, driver):
        """Вспомогательный метод для перехода к форме заказа Драйв."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        return OrderPage(driver)

    @allure.title("Проверка описания тарифа Повседневный")
    @allure.description(
        "Проверка корректного описания тарифа Повседневный в секции превью"
    )
    def test_everyday_fare_description(self, open_main_page):
        """Тест описания тарифа Повседневный в секции превью."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Кликнуть на тариф Повседневный для показа описания"):
            order_page.hover_fare_info_icon("повседневный")

        with allure.step("Проверить текст описания"):
            description_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.EVERYDAY
            assert expected in description_text, (
                f"Ожидалось описание, содержащее '{expected}', получено '{description_text}'"
            )

    @allure.title("Проверка описания тарифа Походный")
    @allure.description(
        "Проверка корректного описания тарифа Походный в секции превью"
    )
    def test_outdoor_fare_description(self, open_main_page):
        """Тест описания тарифа Походный в секции превью."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Кликнуть на тариф Походный для показа описания"):
            order_page.hover_fare_info_icon("походный")

        with allure.step("Проверить текст описания"):
            description_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.OUTDOOR
            assert expected in description_text, (
                f"Ожидалось описание, содержащее '{expected}', получено '{description_text}'"
            )

    @allure.title("Проверка описания тарифа Роскошный")
    @allure.description(
        "Проверка корректного описания тарифа Роскошный в секции превью"
    )
    def test_luxury_fare_description(self, open_main_page):
        """Тест описания тарифа Роскошный в секции превью."""
        order_page = self._navigate_to_drive_order(open_main_page)

        with allure.step("Кликнуть на тариф Роскошный для показа описания"):
            order_page.hover_fare_info_icon("роскошный")

        with allure.step("Проверить текст описания"):
            description_text = order_page.get_tooltip_text()
            expected = DriveFareDescriptions.LUXURY
            assert expected in description_text, (
                f"Ожидалось описание, содержащее '{expected}', получено '{description_text}'"
            )


@allure.feature("Заказ Драйв")
@allure.story("Окно добавления водительских прав")
class TestAddDriverLicenseWindow:
    """Класс тестов для функциональности окна добавления водительских прав."""

    def _navigate_to_license_window(self, driver):
        """Вспомогательный метод для перехода к окну добавления прав."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        # Сначала кликаем на тариф чтобы активировать форму
        order_page.select_everyday_fare()

        # Клик по "Добавить права" для открытия окна прав
        order_page.click_add_license_button()

        return order_page

    @allure.title("Проверка отображения окна добавления прав")
    @allure.description(
        "Проверка отображения окна добавления водительских прав при необходимости"
    )
    def test_license_window_displayed(self, open_main_page):
        """Тест появления окна добавления прав."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Проверить отображение окна добавления прав"):
            assert order_page.is_license_window_displayed(), (
                "Окно добавления водительских прав должно отображаться"
            )

    @allure.title("Проверка наличия всех полей формы прав")
    @allure.description(
        "Проверка наличия всех обязательных полей: "
        "Имя, Фамилия, Дата рождения, Номер"
    )
    def test_all_license_fields_present(self, open_main_page):
        """Тест видимости всех полей формы прав."""
        order_page = self._navigate_to_license_window(open_main_page)

        with allure.step("Проверить наличие всех полей формы прав"):
            missing_fields = []

            if not order_page.is_first_name_field_displayed():
                missing_fields.append("Имя")

            if not order_page.is_last_name_field_displayed():
                missing_fields.append("Фамилия")

            if not order_page.is_date_of_birth_field_displayed():
                missing_fields.append("Дата рождения")

            if not order_page.is_license_number_field_displayed():
                missing_fields.append("Номер")

            assert not missing_fields, (
                f"Отсутствующие поля формы прав: {missing_fields}"
            )


@allure.feature("Заказ Драйв")
@allure.story("Окно совершенного заказа Драйв")
class TestCompletedDriveOrder:
    """Класс тестов для окна совершенного заказа Драйв.

    Тестовый сценарий: Полный флоу заказа Драйв
    Предусловия:
    - Ввести два разных предустановленных адреса
    - Выбрать маршрут Свой
    - Выбрать тип передвижения Драйв
    - Нажать кнопку Забронировать
    - Выбрать тариф
    - Нажать кнопку Добавить права
    - Заполнить форму прав
    """

    def _complete_drive_order(self, driver):
        """Вспомогательный метод для совершения заказа Драйв."""
        main_page = MainPage(driver)
        route_page = RoutePage(driver)
        order_page = OrderPage(driver)

        main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        route_page.select_custom_route()
        route_page.select_drive_transport()
        route_page.click_book()

        # Кликаем на тариф Повседневный
        order_page.select_everyday_fare()

        # Нажимаем кнопку "Добавить права"
        order_page.click_add_license_button()

        # Заполняем форму прав
        order_page.enter_first_name("Владимир")
        order_page.enter_last_name("Набоков")
        order_page.enter_date_of_birth("24.04.1889")
        order_page.enter_license_number("01 01 123456")
        order_page.click_add_license()

        # Нажимаем кнопку "Принято" в окне подтверждения
        order_page.click_license_confirmation()

        # Ждём пока форма заказа снова станет доступна
        order_page.wait_for_order_form_displayed()

        # После подтверждения прав снова выбираем тариф и нажимаем кнопку бронирования
        order_page.select_everyday_fare()
        order_page.click_enter_number_and_order()

        return order_page

    @allure.title("Проверка заголовка окна совершенного заказа Драйв")
    @allure.description(
        "Проверка отображения заголовка 'Машина забронирована' в окне совершенного заказа Драйв"
    )
    @pytest.mark.slow
    def test_drive_order_title(self, open_main_page):
        """Тест заголовка окна совершенного заказа Драйв."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Проверить отображение окна заказа Драйв"):
            assert order_page.is_drive_order_window_displayed(), (
                "Окно совершенного заказа Драйв должно отображаться"
            )

    @allure.title("Проверка отображения таймера бесплатного ожидания")
    @allure.description(
        "Проверка отображения таймера бесплатного ожидания в окне совершенного заказа Драйв"
    )
    @pytest.mark.slow
    def test_free_waiting_timer_displayed(self, open_main_page):
        """Тест видимости таймера бесплатного ожидания."""
        order_page = self._complete_drive_order(open_main_page)

        with allure.step("Проверить отображение таймера бесплатного ожидания"):
            assert order_page.is_free_waiting_timer_displayed(), (
                "Таймер бесплатного ожидания должен отображаться в правом верхнем углу"
            )

    @allure.title("Проверка закрытия окна заказа Драйв при отмене")
    @allure.description(
        "Проверка закрытия окна заказа Драйв при нажатии кнопки Отменить"
    )
    @pytest.mark.slow
    @pytest.mark.xfail(reason="Баг: Кнопка Отменить не работает")
    def test_cancel_closes_drive_order(self, open_main_page):
        """Тест отмены заказа Драйв."""
        order_page = self._complete_drive_order(open_main_page)


        with allure.step("Нажать кнопку Отменить"):
            order_page.click_cancel()

        with allure.step("Проверить закрытие окна заказа"):
            assert order_page.is_order_window_closed(), (
                "Окно заказа Драйв должно закрыться после отмены"
            )
