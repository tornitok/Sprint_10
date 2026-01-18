"""Тесты на функциональность 'Отрисовка маршрута'."""

import allure
from pages.main_page import MainPage
from test_data.addresses import Addresses


@allure.feature("Отрисовка маршрута")
@allure.story("Визуализация маршрута на карте")
class TestRouteRendering:
    """Класс тестов для функциональности отрисовки маршрута.

    Тестовый сценарий 1: Отрисовка маршрута
    Предусловия: Ввести два разных предустановленных адреса в поля Откуда и Куда
    """

    @allure.title("Проверка отображения карты на главной странице")
    @allure.description("Проверка видимости контейнера карты при загрузке страницы")
    def test_map_is_displayed(self, open_main_page):
        """Тест отображения карты на главной странице."""
        main_page = MainPage(open_main_page)

        with allure.step("Проверить отображение карты"):
            assert main_page.is_map_displayed(), "Карта должна отображаться на главной странице"

    @allure.title("Проверка ввода адресов в поля ввода")
    @allure.description("Проверка корректного ввода адресов в поля ввода")
    def test_address_input_fields_accept_text(self, open_main_page):
        """Тест принятия и сохранения текста полями ввода адресов."""
        main_page = MainPage(open_main_page)

        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Проверить значение поля Откуда"):
            from_value = main_page.get_from_input_value()
            assert from_value == Addresses.FROM_ADDRESS, f"Ожидалось '{Addresses.FROM_ADDRESS}', получено '{from_value}'"

        with allure.step("Проверить значение поля Куда"):
            to_value = main_page.get_to_input_value()
            assert to_value == Addresses.TO_ADDRESS, f"Ожидалось '{Addresses.TO_ADDRESS}', получено '{to_value}'"

    @allure.title("Проверка отрисовки маршрута на карте")
    @allure.description(
        "Проверка отрисовки маршрута на карте после ввода "
        "двух разных предустановленных адресов"
    )
    def test_route_rendered_on_map(self, open_main_page):
        """Тест отрисовки маршрута после ввода валидных адресов."""
        main_page = MainPage(open_main_page)

        with allure.step("Построить маршрут с двумя разными предустановленными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Проверить отображение линии маршрута на карте"):
            assert main_page.is_route_line_displayed(), (
                "Линия маршрута должна отображаться на карте после построения маршрута"
            )

    @allure.title("Проверка отображения маркера начала маршрута на карте")
    @allure.description(
        "Проверка отображения маркера начальной точки на карте "
        "после построения маршрута"
    )
    def test_start_marker_displayed(self, open_main_page):
        """Тест появления маркера начальной точки на карте."""
        main_page = MainPage(open_main_page)

        with allure.step("Построить маршрут с двумя разными предустановленными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Проверить отображение маркера начальной точки"):
            assert main_page.is_start_marker_displayed(), (
                "Маркер начальной точки должен быть виден на карте"
            )

    @allure.title("Проверка отображения маркера конца маршрута на карте")
    @allure.description(
        "Проверка отображения маркера конечной точки на карте "
        "после построения маршрута"
    )
    def test_end_marker_displayed(self, open_main_page):
        """Тест появления маркера конечной точки на карте."""
        main_page = MainPage(open_main_page)

        with allure.step("Построить маршрут с двумя разными предустановленными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Проверить отображение маркера конечной точки"):
            assert main_page.is_end_marker_displayed(), (
                "Маркер конечной точки должен быть виден на карте"
            )

    @allure.title("Проверка отрисовки маршрута при обратном порядке адресов")
    @allure.description(
        "Проверка корректной отрисовки маршрута при вводе адресов "
        "в обратном порядке (адрес Куда в поле Откуда и наоборот)"
    )
    def test_route_rendered_with_reversed_addresses(self, open_main_page):
        """Тест отрисовки маршрута с обменом адресов местами."""
        main_page = MainPage(open_main_page)

        with allure.step("Построить маршрут с обратным порядком адресов"):
            main_page.build_route(Addresses.TO_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Проверить отображение линии маршрута"):
            assert main_page.is_route_line_displayed(), (
                "Маршрут должен отображаться при обратном порядке адресов"
            )

        with allure.step("Проверить отображение обоих маркеров"):
            assert main_page.is_start_marker_displayed(), (
                "Маркер начала должен быть виден при обратном порядке адресов"
            )
            assert main_page.is_end_marker_displayed(), (
                "Маркер конца должен быть виден при обратном порядке адресов"
            )
