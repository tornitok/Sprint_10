import allure
from pages.main_page import MainPage


@allure.feature('Построение маршрута')
@allure.story('Отрисовка маршрута на карте')
class TestRouteDrawing:
    """
    Тесты для проверки отрисовки маршрута между предустановленными адресами
    """

    @allure.title('Отображение точек маршрута: Хамовнический вал -> Зубовский бульвар')
    @allure.description(
        'Проверка отображения двух точек (начала и конца маршрута) на карте '
        'при вводе адресов "Хамовнический вал, 34" и "Зубовский бульвар, 37"'
    )
    def test_route_points_hamovnichesky_to_zubovsky(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Проверить, что карта видна'):
            assert main_page.is_map_visible(), "Карта не отображается на странице"

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться отображения маршрута на карте'):
            route_displayed = main_page.wait_for_route_to_display(timeout=10)
            assert route_displayed, "Маршрут не отобразился на карте в течение 10 секунд"

        with allure.step('Проверить количество точек маршрута на карте'):
            markers_count = main_page.get_map_markers_count()
            assert markers_count >= 2, \
                f"На карте должно быть минимум 2 точки (начало и конец маршрута), найдено: {markers_count}"

    @allure.title('Отображение точек маршрута: Зубовский бульвар -> Хамовнический вал')
    @allure.description(
        'Проверка отображения двух точек (начала и конца маршрута) на карте '
        'при вводе адресов "Зубовский бульвар, 37" и "Хамовнический вал, 34" (обратный порядок)'
    )
    def test_route_points_zubovsky_to_hamovnichesky(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Проверить, что карта видна'):
            assert main_page.is_map_visible(), "Карта не отображается на странице"

        with allure.step('Ввести адрес начала маршрута: Зубовский бульвар, 37'):
            main_page.enter_from_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Ввести адрес конца маршрута: Хамовнический вал, 34'):
            main_page.enter_to_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Дождаться отображения маршрута на карте'):
            route_displayed = main_page.wait_for_route_to_display(timeout=10)
            assert route_displayed, "Маршрут не отобразился на карте в течение 10 секунд"

        with allure.step('Проверить количество точек маршрута на карте'):
            markers_count = main_page.get_map_markers_count()
            assert markers_count >= 2, \
                f"На карте должно быть минимум 2 точки (начало и конец маршрута), найдено: {markers_count}"
