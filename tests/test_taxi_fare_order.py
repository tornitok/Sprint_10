"""Тесты на функциональность 'Заказ тарифа Такси'."""

import allure
import pytest
from test_data.addresses import (
    TaxiFares,
    TaxiFareDescriptions,
)


@allure.feature("Заказ тарифа Такси")
@allure.story("Выбор тарифа такси и форма заказа")
class TestTaxiFareOrder:
    """Класс тестов для функциональности заказа тарифа такси.

    Тестовый сценарий 4: Заказ тарифа Такси
    Предусловия:
    - Ввести два разных предустановленных адреса
    - Выбрать маршрут Быстрый
    - Нажать кнопку Вызвать такси
    """

    @allure.title("Проверка открытия формы заказа такси после нажатия Вызвать такси")
    @allure.description(
        "Проверка открытия формы заказа такси после нажатия кнопки Вызвать такси"
    )
    def test_taxi_order_form_opens(self, navigate_to_taxi_order_form):
        """Тест отображения формы заказа такси."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Проверить отображение формы заказа"):
            assert order_page.is_order_form_displayed(), (
                "Форма заказа такси должна отображаться после нажатия Вызвать такси"
            )

    @allure.title("Проверка наличия 6 тарифов в форме заказа такси")
    @allure.description(
        "Проверка наличия 6 тарифов в форме согласно спецификации"
    )
    def test_order_form_contains_six_fares(self, navigate_to_taxi_order_form):
        """Тест отображения ровно 6 тарифов."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Проверить отображение 6 тарифов"):
            fares_count = order_page.get_fares_count()
            assert fares_count == TaxiFares.FARES_COUNT, (
                f"Ожидалось {TaxiFares.FARES_COUNT} тарифов, найдено {fares_count}"
            )

    @allure.title("Проверка наличия ровно одного активного тарифа по умолчанию")
    @allure.description(
        "Проверка выбора ровно одного тарифа по умолчанию"
    )
    def test_one_fare_active_by_default(self, navigate_to_taxi_order_form):
        """Тест предвыбора одного тарифа."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Проверить активность ровно одного тарифа"):
            assert order_page.is_one_fare_active(), (
                "Ровно один тариф должен быть активен по умолчанию"
            )

    @allure.title("Проверка наличия всех 6 указанных тарифов")
    @allure.description(
        "Проверка отображения всех тарифов согласно спецификации: "
        "Рабочий, Сонный, Отпускной, Разговорчивый, Утешительный, Глянцевый"
    )
    def test_all_specified_fares_present(self, navigate_to_taxi_order_form):
        """Тест доступности всех указанных тарифов."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Проверить видимость всех тарифов"):
            missing_fares = []
            for fare in TaxiFares.ALL_FARES:
                if not order_page.is_fare_visible(fare):
                    missing_fares.append(fare)

            assert not missing_fares, (
                f"Отсутствующие тарифы: {missing_fares}. "
                f"Ожидались все: {TaxiFares.ALL_FARES}"
            )


@allure.feature("Заказ тарифа Такси")
@allure.story("Всплывающие подсказки описания тарифов")
class TestFareDescriptionTooltips:
    """Класс тестов для функциональности всплывающих подсказок описания тарифов."""

    @allure.title("Проверка соответствия всех описаний тарифов спецификации")
    @allure.description(
        "Проверка соответствия текста всех всплывающих подсказок тарифов спецификации"
    )
    @pytest.mark.parametrize("fare,expected_description", [
        (TaxiFares.BUSINESS, TaxiFareDescriptions.BUSINESS),
        pytest.param(TaxiFares.SLEEPY, TaxiFareDescriptions.SLEEPY,
                     marks=pytest.mark.xfail(reason="Баг: Описания тарифов Сонный и Разговорчивый перепутаны")),
        (TaxiFares.VACATION, TaxiFareDescriptions.VACATION),
        pytest.param(TaxiFares.TALKATIVE, TaxiFareDescriptions.TALKATIVE,
                     marks=pytest.mark.xfail(reason="Баг: Описания тарифов Сонный и Разговорчивый перепутаны")),
        (TaxiFares.COMFORTING, TaxiFareDescriptions.COMFORTING),
        (TaxiFares.GLOSSY, TaxiFareDescriptions.GLOSSY),
    ])
    def test_fare_tooltip_parametrized(self, navigate_to_taxi_order_form, fare, expected_description):
        """Параметризованный тест всех всплывающих подсказок тарифов."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step(f"Навести на иконку информации тарифа {fare}"):
            order_page.hover_fare_info_icon(fare)

        with allure.step("Проверить соответствие текста подсказки спецификации"):
            tooltip_text = order_page.get_tooltip_text()
            assert expected_description in tooltip_text, (
                f"Для тарифа {fare}: ожидалось '{expected_description}', "
                f"получено '{tooltip_text}'"
            )


@allure.feature("Заказ тарифа Такси")
@allure.story("Поля формы заказа")
class TestTaxiOrderFormFields:
    """Класс тестов для полей формы заказа такси."""

    @allure.title("Проверка наличия всех обязательных полей формы")
    @allure.description(
        "Проверка наличия всех обязательных полей в форме заказа: "
        "телефон, способ оплаты, комментарий, требования к заказу"
    )
    def test_all_form_fields_present(self, navigate_to_taxi_order_form):
        """Тест отображения всех обязательных полей."""
        _, _, order_page = navigate_to_taxi_order_form

        with allure.step("Проверить наличие всех полей формы"):
            missing_fields = []

            if not order_page.is_phone_field_displayed():
                missing_fields.append("Телефон")

            if not order_page.is_payment_method_field_displayed():
                missing_fields.append("Способ оплаты")

            if not order_page.is_comment_field_displayed():
                missing_fields.append("Комментарий водителю")

            if not order_page.is_requirements_field_displayed():
                missing_fields.append("Требования к заказу")

            assert not missing_fields, (
                f"Отсутствующие поля формы: {missing_fields}"
            )
