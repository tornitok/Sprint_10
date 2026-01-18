"""Тесты на функциональность 'Полный сценарий заказа такси'."""

import allure
import pytest
from test_data.addresses import ExpectedTexts


@allure.feature("Полный сценарий заказа такси")
@allure.story("Полный флоу заказа такси")
class TestTaxiOrderFullScenario:
    """Класс тестов для полного флоу заказа такси.

    Тестовый сценарий 5: Заказ такси - Полный сценарий
    Предусловия:
    - Ввести два разных предустановленных адреса
    - Выбрать маршрут Быстрый
    - Нажать кнопку Вызвать такси
    """

    @allure.title("Проверка открытия окна поиска машины после отправки заказа")
    @allure.description(
        "Проверка появления окна поиска машины после выбора тарифа Рабочий "
        "и нажатия кнопки Ввести номер и заказать"
    )
    def test_car_search_window_opens(self, navigate_to_taxi_order_form):
        """Тест появления окна поиска машины после отправки заказа."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий"):
            order_page.select_business_fare()

        with allure.step("Нажать кнопку 'Ввести номер и заказать'"):
            order_page.click_enter_number_and_order()

        with allure.step("Проверить отображение окна поиска машины"):
            assert order_page.is_car_search_window_displayed(), (
                "Окно поиска машины должно отображаться после отправки заказа"
            )

    @allure.title("Проверка заголовка окна поиска машины")
    @allure.description(
        "Проверка отображения заголовка 'Поиск машины' в окне поиска"
    )
    def test_car_search_window_title(self, navigate_to_taxi_order_form):
        """Тест корректности заголовка окна поиска машины."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Проверить заголовок окна поиска"):
            title = order_page.get_car_search_title()
            assert ExpectedTexts.SEARCHING_FOR_CAR in title, (
                f"Ожидался заголовок, содержащий '{ExpectedTexts.SEARCHING_FOR_CAR}', "
                f"получено '{title}'"
            )

    @allure.title("Проверка отображения таймера обратного отсчета в окне поиска")
    @allure.description(
        "Проверка отображения таймера обратного отсчета в окне поиска машины"
    )
    def test_search_timer_displayed(self, navigate_to_taxi_order_form):
        """Тест видимости таймера обратного отсчета в окне поиска."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Проверить отображение таймера обратного отсчета"):
            assert order_page.is_search_timer_displayed(), (
                "Таймер обратного отсчета должен отображаться в правом верхнем углу"
            )

    @allure.title("Проверка наличия кнопок Отменить и Детали в окне поиска")
    @allure.description(
        "Проверка наличия кнопок Отменить и Детали в окне поиска машины"
    )
    def test_search_window_buttons_displayed(self, navigate_to_taxi_order_form):
        """Тест видимости кнопок Отменить и Детали в окне поиска."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Проверить отображение окна поиска"):
            assert order_page.is_car_search_window_displayed(), (
                "Окно поиска должно отображаться"
            )


@allure.feature("Полный сценарий заказа такси")
@allure.story("Проверка совершенного заказа")
class TestCompletedTaxiOrder:
    """Класс тестов для проверки совершенного заказа такси."""

    @allure.title("Проверка отображения окна совершенного заказа после поиска")
    @allure.description(
        "Проверка отображения окна совершенного заказа "
        "после завершения таймера поиска"
    )
    @pytest.mark.slow
    def test_completed_order_window_displayed(self, navigate_to_taxi_order_form):
        """Тест появления окна совершенного заказа после завершения поиска."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий и отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Дождаться завершения поиска машины"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Проверить отображение окна совершенного заказа"):
            assert order_page.is_completed_order_displayed(), (
                "Окно совершенного заказа должно отображаться после поиска"
            )

    @allure.title("Проверка формата заголовка заказа 'N мин. и приедет'")
    @allure.description(
        "Проверка отображения заголовка 'N мин. и приедет' в окне совершенного заказа"
    )
    @pytest.mark.slow
    def test_order_title_format(self, navigate_to_taxi_order_form):
        """Тест формата заголовка с временем прибытия."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий и отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Дождаться завершения поиска машины"):
            order_page.wait_for_search_complete(timeout=90)

        with allure.step("Проверить формат заголовка заказа"):
            title = order_page.get_order_title()
            assert ExpectedTexts.MINUTES_AND_ARRIVING in title, (
                f"Ожидался заголовок, содержащий '{ExpectedTexts.MINUTES_AND_ARRIVING}', "
                f"получено '{title}'"
            )

    @allure.title("Проверка отображения номера машины")
    @allure.description(
        "Проверка отображения номера машины в окне совершенного заказа"
    )
    @pytest.mark.slow
    def test_car_number_displayed(self, navigate_to_taxi_order_form):
        """Тест видимости номера машины в совершенном заказе."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий и отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Дождаться завершения поиска машины"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Проверить отображение номера машины"):
            assert order_page.is_car_number_displayed(), (
                "Номер машины должен отображаться в окне совершенного заказа"
            )

    @allure.title("Проверка отображения картинки тарифа")
    @allure.description(
        "Проверка отображения картинки тарифа в окне совершенного заказа"
    )
    @pytest.mark.slow
    @pytest.mark.xfail(reason="Баг: Картинка тарифа не отображается")
    def test_fare_image_displayed(self, navigate_to_taxi_order_form):
        """Тест видимости картинки тарифа в совершенном заказе."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий и отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Дождаться завершения поиска машины"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Проверить отображение картинки тарифа"):
            assert order_page.is_fare_image_displayed(), (
                "Картинка тарифа должна отображаться в правом верхнем углу"
            )

    @allure.title("Проверка отображения информации о водителе")
    @allure.description(
        "Проверка отображения блока информации о водителе в окне совершенного заказа"
    )
    @pytest.mark.slow
    def test_driver_info_displayed(self, navigate_to_taxi_order_form):
        """Тест видимости информации о водителе в совершенном заказе."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Выбрать тариф Рабочий и отправить заказ"):
            order_page.select_business_fare()
            order_page.click_enter_number_and_order()

        with allure.step("Дождаться завершения поиска машины"):
            order_page.wait_for_search_complete(timeout=60)

        with allure.step("Проверить отображение блока информации о водителе"):
            assert order_page.is_driver_info_displayed(), (
                "Блок информации о водителе должен отображаться"
            )


@allure.feature("Полный сценарий заказа такси")
@allure.story("Проверка деталей заказа")
class TestOrderDetails:
    """Класс тестов для проверки деталей заказа."""

    @allure.title("Проверка открытия окна деталей заказа")
    @allure.description(
        "Проверка открытия окна деталей заказа при нажатии кнопки Детали "
        "в блоке 'Еще про поездку'"
    )
    @pytest.mark.slow
    def test_order_details_window_opens(self, complete_taxi_order):
        """Тест открытия окна деталей заказа по клику."""
        order_page = complete_taxi_order

        with allure.step("Нажать кнопку Детали"):
            order_page.click_details()

        with allure.step("Проверить отображение окна деталей заказа"):
            assert order_page.is_order_details_displayed(), (
                "Окно деталей заказа должно отображаться"
            )

    @allure.title("Проверка соответствия стоимости в деталях выбранному тарифу")
    @allure.description(
        "Проверка соответствия стоимости в деталях заказа "
        "стоимости, отображавшейся при выборе тарифа"
    )
    @pytest.mark.slow
    def test_cost_matches_fare_selection(self, complete_taxi_order):
        """Тест соответствия стоимости заказа стоимости тарифа."""
        order_page = complete_taxi_order

        with allure.step("Нажать кнопку Детали"):
            order_page.click_details()

        with allure.step("Проверить отображение стоимости в деталях"):
            details_cost = order_page.get_trip_cost()
            assert details_cost, (
                "Стоимость должна отображаться в деталях заказа"
            )


@allure.feature("Полный сценарий заказа такси")
@allure.story("Отмена заказа")
class TestOrderCancellation:
    """Класс тестов для функциональности отмены заказа."""

    @allure.title("Проверка закрытия окна при отмене заказа")
    @allure.description(
        "Проверка закрытия окна заказа при нажатии кнопки Отмена"
    )
    @pytest.mark.slow
    @pytest.mark.xfail(reason="Баг: Кнопка Отменить не работает")
    def test_cancel_closes_order_window(self, complete_taxi_order):
        """Тест закрытия окна при отмене заказа."""
        order_page = complete_taxi_order

        with allure.step("Нажать кнопку Отменить"):
            order_page.click_cancel()

        with allure.step("Проверить закрытие окна заказа"):
            assert order_page.is_order_window_closed(), (
                "Окно заказа должно закрыться после отмены"
            )
