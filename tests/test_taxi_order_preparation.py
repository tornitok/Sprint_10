"""Тесты на функциональность 'Подготовка к заказу такси'."""

import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from test_data.addresses import Addresses, RouteTypes


@allure.feature("Подготовка к заказу такси")
@allure.story("Подготовка заказа такси перед подтверждением")
class TestTaxiOrderPreparation:
    """Класс тестов для функциональности подготовки к заказу такси.

    Тестовый сценарий 3: Подготовка к заказу такси
    Предусловия: Ввести два разных предустановленных адреса в поля Откуда и Куда
    """

    @allure.title("Проверка переключения на маршрут Оптимальный")
    @allure.description(
        "Проверка смены активного таба при переключении на маршрут Оптимальный"
    )
    def test_switch_to_optimal_route(self, open_main_page):
        """Тест переключения на вид маршрута Оптимальный."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Оптимальный"):
            route_page.select_optimal_route()

        with allure.step("Проверить активность таба Оптимальный"):
            assert route_page.is_optimal_tab_active(), (
                "Таб Оптимальный должен быть активным после выбора"
            )

    @allure.title("Проверка переключения на маршрут Быстрый")
    @allure.description(
        "Проверка смены активного таба при переключении на маршрут Быстрый"
    )
    def test_switch_to_fast_route(self, open_main_page):
        """Тест переключения на вид маршрута Быстрый."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Быстрый"):
            route_page.select_fast_route()

        with allure.step("Проверить активность таба Быстрый"):
            assert route_page.is_fast_tab_active(), (
                "Таб Быстрый должен быть активным после выбора"
            )

    @allure.title("Проверка пересчета времени и стоимости при переключении вида маршрута")
    @allure.description(
        "Проверка пересчета времени и стоимости при переключении "
        "между видами маршрута Оптимальный и Быстрый"
    )
    def test_route_time_cost_recalculated(self, open_main_page):
        """Тест изменения времени и стоимости при переключении видов маршрута."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Оптимальный и получить значения"):
            route_page.select_optimal_route()
            optimal_time = route_page.get_route_travel_time()
            optimal_cost = route_page.get_route_cost()

        with allure.step("Переключиться на маршрут Быстрый и получить значения"):
            route_page.select_fast_route()
            fast_time = route_page.get_route_travel_time()
            fast_cost = route_page.get_route_cost()

        with allure.step("Проверить пересчет значений"):
            values_changed = (optimal_time != fast_time) or (optimal_cost != fast_cost)
            assert values_changed, (
                f"Время или стоимость должны измениться при переключении маршрутов. "
                f"Оптимальный: время={optimal_time}, стоимость={optimal_cost}. "
                f"Быстрый: время={fast_time}, стоимость={fast_cost}"
            )

    @allure.title("Проверка переключения на маршрут Свой")
    @allure.description(
        "Проверка смены активного таба при переключении на маршрут Свой"
    )
    def test_switch_to_custom_route(self, open_main_page):
        """Тест переключения на вид маршрута Свой."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Свой"):
            route_page.select_custom_route()

        with allure.step("Проверить активность таба Свой"):
            assert route_page.is_custom_tab_active(), (
                "Таб Свой должен быть активным после выбора"
            )

    @allure.title("Проверка активности типов передвижения при маршруте Свой")
    @allure.description(
        "Проверка активности всех типов передвижения при выборе маршрута Свой: "
        "Машина, Пешком, Такси, Велосипед, Самокат, Драйв"
    )
    @pytest.mark.xfail(reason="Баг: Не все типы передвижения отображаются")
    def test_custom_route_transport_types_active(self, open_main_page):
        """Тест доступности всех типов передвижения при маршруте Свой."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Свой"):
            route_page.select_custom_route()

        with allure.step("Проверить отображение селектора типов передвижения"):
            assert route_page.is_transport_selector_displayed(), (
                "Селектор типов передвижения должен отображаться для маршрута Свой"
            )

        with allure.step("Проверить видимость типа Машина"):
            assert route_page.is_car_transport_active(), (
                "Тип передвижения Машина должен быть виден"
            )

        with allure.step("Проверить видимость типа Пешком"):
            assert route_page.is_walking_transport_visible(), (
                "Тип передвижения Пешком должен быть виден"
            )

        with allure.step("Проверить видимость типа Такси"):
            assert route_page.is_taxi_transport_visible(), (
                "Тип передвижения Такси должен быть виден"
            )

        with allure.step("Проверить видимость типа Велосипед"):
            assert route_page.is_bicycle_transport_visible(), (
                "Тип передвижения Велосипед должен быть виден"
            )

        with allure.step("Проверить видимость типа Самокат"):
            assert route_page.is_scooter_transport_visible(), (
                "Тип передвижения Самокат должен быть виден"
            )

        with allure.step("Проверить видимость типа Драйв"):
            assert route_page.is_drive_transport_visible(), (
                "Тип передвижения Драйв должен быть виден"
            )

    @allure.title("Проверка активности кнопки Вызвать такси при маршруте Быстрый")
    @allure.description(
        "Проверка активности кнопки Вызвать такси при выборе вида маршрута Быстрый"
    )
    def test_call_taxi_button_active_on_fast_route(self, open_main_page):
        """Тест активности кнопки Вызвать такси при маршруте Быстрый."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Быстрый"):
            route_page.select_fast_route()

        with allure.step("Проверить отображение кнопки Вызвать такси"):
            assert route_page.is_call_taxi_button_displayed(), (
                "Кнопка Вызвать такси должна отображаться"
            )

        with allure.step("Проверить активность кнопки Вызвать такси"):
            assert route_page.is_call_taxi_button_enabled(), (
                "Кнопка Вызвать такси должна быть активна при выборе маршрута Быстрый"
            )

    @allure.title("Проверка активности кнопки Забронировать при Свой + Драйв")
    @allure.description(
        "Проверка активности кнопки Забронировать при выборе маршрута Свой "
        "и типа передвижения Драйв"
    )
    def test_book_button_active_on_custom_drive(self, open_main_page):
        """Тест активности кнопки Забронировать при маршруте Свой с типом Драйв."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с разными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Выбрать маршрут Свой"):
            route_page.select_custom_route()

        with allure.step("Выбрать тип передвижения Драйв"):
            route_page.select_drive_transport()

        with allure.step("Проверить отображение кнопки Забронировать"):
            assert route_page.is_book_button_displayed(), (
                "Кнопка Забронировать должна отображаться"
            )

        with allure.step("Проверить активность кнопки Забронировать"):
            assert route_page.is_book_button_enabled(), (
                "Кнопка Забронировать должна быть активна при выборе Свой + Драйв"
            )
