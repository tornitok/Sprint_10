"""Тесты на функциональность 'Отрисовка блока с выбором маршрута'."""

import allure
from pages.main_page import MainPage
from pages.route_page import RoutePage
from test_data.addresses import Addresses, ExpectedTexts


@allure.feature("Блок выбора маршрута")
@allure.story("Функциональность блока выбора маршрута")
class TestRouteOptionsBlock:
    """Класс тестов для функциональности блока выбора маршрута.

    Тестовый сценарий 2: Отрисовка блока с выбором маршрута
    """

    @allure.title("Сценарий А: Проверка отображения блока выбора маршрута при разных адресах")
    @allure.description(
        "Проверка появления блока выбора маршрута под полями ввода адресов "
        "при вводе двух разных предустановленных адресов"
    )
    def test_route_options_displayed_with_different_addresses(self, open_main_page):
        """Тест отображения блока выбора маршрута после построения маршрута с разными адресами."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с двумя разными предустановленными адресами"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Проверить отображение блока выбора маршрута"):
            assert route_page.is_route_options_displayed(), (
                "Блок выбора маршрута должен отображаться под полями ввода адресов"
            )

    @allure.title("Сценарий Б: Проверка отображения блока выбора маршрута при одинаковых адресах")
    @allure.description(
        "Проверка отображения блока выбора маршрута при вводе одного и того же "
        "предустановленного адреса в оба поля Откуда и Куда"
    )
    def test_route_options_displayed_with_same_addresses(self, open_main_page):
        """Тест отображения блока выбора маршрута при одинаковых адресах."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с одинаковым адресом в обоих полях"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Проверить отображение блока выбора маршрута"):
            assert route_page.is_route_options_displayed(), (
                "Блок выбора маршрута должен отображаться даже при одинаковых адресах"
            )

    @allure.title("Сценарий Б: Проверка отображения типа маршрута Авто при одинаковых адресах")
    @allure.description(
        "Проверка отображения типа маршрута 'Авто' при одинаковых адресах"
    )
    def test_same_address_shows_auto_route_type(self, open_main_page):
        """Тест отображения типа маршрута Авто при одинаковых адресах."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с одинаковым адресом"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Проверить отображение типа маршрута 'Авто'"):
            route_type = route_page.get_route_type_text()
            assert ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE in route_type, (
                f"Ожидался тип маршрута, содержащий '{ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE}', "
                f"получено '{route_type}'"
            )

    @allure.title("Сценарий Б: Проверка отображения стоимости Бесплатно при одинаковых адресах")
    @allure.description(
        "Проверка отображения стоимости 'Бесплатно' при одинаковых адресах"
    )
    def test_same_address_shows_free_cost(self, open_main_page):
        """Тест отображения стоимости Бесплатно при одинаковых адресах."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с одинаковым адресом"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Проверить отображение стоимости 'Бесплатно'"):
            cost = route_page.get_cost_text()
            assert ExpectedTexts.SAME_ADDRESS_COST in cost, (
                f"Ожидалась стоимость, содержащая '{ExpectedTexts.SAME_ADDRESS_COST}', "
                f"получено '{cost}'"
            )

    @allure.title("Сценарий Б: Проверка отображения нулевого времени в пути при одинаковых адресах")
    @allure.description(
        "Проверка отображения времени в пути '0 мин.' при одинаковых адресах"
    )
    def test_same_address_shows_zero_travel_time(self, open_main_page):
        """Тест отображения нулевого времени в пути при одинаковых адресах."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с одинаковым адресом"):
            main_page.build_route(Addresses.FROM_ADDRESS, Addresses.FROM_ADDRESS)

        with allure.step("Проверить отображение времени '0 мин.'"):
            travel_time = route_page.get_route_travel_time()
            assert ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME in travel_time, (
                f"Ожидалось время, содержащее '{ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME}', "
                f"получено '{travel_time}'"
            )

    @allure.title("Сценарий Б: Проверка полного содержимого блока при одинаковых адресах")
    @allure.description(
        "Проверка отображения всего ожидаемого текста при одинаковых адресах: "
        "Авто, Бесплатно, В пути 0 мин."
    )
    def test_same_address_complete_block_content(self, open_main_page):
        """Тест полной проверки содержимого для маршрута с одинаковыми адресами."""
        main_page = MainPage(open_main_page)
        route_page = RoutePage(open_main_page)

        with allure.step("Построить маршрут с одинаковым адресом"):
            main_page.build_route(Addresses.TO_ADDRESS, Addresses.TO_ADDRESS)

        with allure.step("Проверить отображение блока выбора маршрута"):
            assert route_page.is_route_options_displayed(), (
                "Блок выбора маршрута должен отображаться"
            )

        with allure.step("Проверить наличие всех ожидаемых текстов"):
            route_type = route_page.get_route_type_text()
            cost = route_page.get_cost_text()
            travel_time = route_page.get_route_travel_time()

            errors = []
            if ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE not in route_type:
                errors.append(
                    f"Тип маршрута: ожидалось '{ExpectedTexts.SAME_ADDRESS_ROUTE_TYPE}', "
                    f"получено '{route_type}'"
                )
            if ExpectedTexts.SAME_ADDRESS_COST not in cost:
                errors.append(
                    f"Стоимость: ожидалось '{ExpectedTexts.SAME_ADDRESS_COST}', получено '{cost}'"
                )
            if ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME not in travel_time:
                errors.append(
                    f"Время в пути: ожидалось '{ExpectedTexts.SAME_ADDRESS_TRAVEL_TIME}', "
                    f"получено '{travel_time}'"
                )

            assert not errors, "\n".join(errors)
