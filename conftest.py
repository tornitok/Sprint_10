"""Фикстуры для тестов."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
from test_data.addresses import Addresses


def pytest_configure(config):
    """Регистрация пользовательских pytest маркеров."""
    config.addinivalue_line("markers", "slow: помечает тесты как медленные (исключить с помощью '-m \"not slow\"')")


@pytest.fixture
def get_chrome_options():
    """Получение опций Chrome браузера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_web_driver(get_chrome_options):
    """Создание и закрытие веб-драйвера."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=get_chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(get_web_driver):
    """Фикстура открытия главной страницы и возврата драйвера."""
    driver = get_web_driver
    driver.get("https://ez-route.stand.praktikum-services.ru/")
    driver.maximize_window()
    return driver


@pytest.fixture
def navigate_to_taxi_order_form(open_main_page):
    """Фикстура для перехода к форме заказа такси.

    Возвращает кортеж (main_page, route_page, order_page).
    """
    driver = open_main_page
    main_page = MainPage(driver)
    route_page = RoutePage(driver)

    main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
    route_page.select_fast_route()
    route_page.click_call_taxi()

    return main_page, route_page, OrderPage(driver)


@pytest.fixture
def complete_taxi_order(open_main_page):
    """Фикстура для совершения заказа такси и ожидания завершения.

    Возвращает order_page.
    """
    driver = open_main_page
    main_page = MainPage(driver)
    route_page = RoutePage(driver)
    order_page = OrderPage(driver)

    main_page.build_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
    route_page.select_fast_route()
    route_page.click_call_taxi()
    order_page.select_business_fare()

    order_page.click_enter_number_and_order()
    order_page.wait_for_search_complete(timeout=60)

    return order_page

