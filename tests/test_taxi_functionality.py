import allure
from pages.main_page import MainPage


@allure.feature('Подготовка к заказу такси')
@allure.story('Переключение видов маршрута и типов передвижения')
class TestRouteTypesSwitching:
    """
    Тесты для проверки переключения между видами маршрута и типами передвижения
    """

    @allure.title('Переключение между видами маршрута Оптимальный и Быстрый')
    @allure.description(
        'Проверка смены активного таба и пересчета времени и стоимости '
        'при переключении между видами маршрута Оптимальный и Быстрый'
    )
    def test_switch_between_optimal_and_fast_route_types(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Получить стоимость и время для вида маршрута Оптимальный'):
            optimal_cost = main_page.get_route_cost()
            optimal_time = main_page.get_route_time()

        with allure.step('Переключиться на вид маршрута Быстрый'):
            main_page.click_route_type_fast()

        with allure.step('Проверить, что активный таб изменился на Быстрый'):
            active_route_type = main_page.get_active_route_type()
            assert active_route_type == 'Быстрый', \
                f"Активный вид маршрута должен быть 'Быстрый', получено: {active_route_type}"

        with allure.step('Получить стоимость и время для вида маршрута Быстрый'):
            fast_cost = main_page.get_route_cost()
            fast_time = main_page.get_route_time()

        with allure.step('Проверить, что произошел пересчет времени или стоимости'):
            # Время или стоимость должны отличаться при переключении
            assert (optimal_cost != fast_cost) or (optimal_time != fast_time), \
                "При переключении вида маршрута должен произойти пересчет времени или стоимости"

    @allure.title('Переключение на вид маршрута Свой активирует типы передвижения')
    @allure.description(
        'Проверка что при переключении на вид маршрута Свой '
        'становятся активны 6 типов передвижения'
    )
    def test_custom_route_type_activates_transport_types(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Переключиться на вид маршрута Свой'):
            main_page.click_route_type_custom()

        with allure.step('Проверить, что активный таб изменился на Свой'):
            active_route_type = main_page.get_active_route_type()
            assert active_route_type == 'Свой', \
                f"Активный вид маршрута должен быть 'Свой', получено: {active_route_type}"

        with allure.step('Проверить, что типы передвижения видны'):
            assert main_page.are_transport_types_visible(), \
                "Типы передвижения должны быть видны при выборе вида маршрута Свой"

        with allure.step('Проверить, что доступно 6 типов передвижения'):
            transport_types_count = main_page.get_transport_types_count()
            assert transport_types_count == 6, \
                f"Должно быть 6 типов передвижения, найдено: {transport_types_count}"

    @allure.title('Кнопка Вызвать такси активна при виде маршрута Быстрый')
    @allure.description('Проверка активности кнопки Вызвать такси при выборе вида маршрута Быстрый')
    def test_call_taxi_button_active_for_fast_route(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Выбрать вид маршрута Быстрый'):
            main_page.click_route_type_fast()

        with allure.step('Проверить, что кнопка Вызвать такси активна'):
            assert main_page.is_call_taxi_button_active(), \
                "Кнопка 'Вызвать такси' должна быть активна при выборе вида маршрута Быстрый"

    @allure.title('Кнопка Забронировать активна при типе передвижения Драйв')
    @allure.description(
        'Проверка активности кнопки Забронировать '
        'при выборе вида маршрута Свой и типа передвижения Драйв'
    )
    def test_book_button_active_for_drive_transport(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Выбрать вид маршрута Свой'):
            main_page.click_route_type_custom()

        with allure.step('Выбрать тип передвижения Драйв'):
            main_page.click_transport_type_drive()

        with allure.step('Проверить, что кнопка Забронировать активна'):
            assert main_page.is_book_button_active(), \
                "Кнопка 'Забронировать' должна быть активна при выборе типа передвижения Драйв"


@allure.feature('Заказ тарифа Такси')
@allure.story('Форма заказа такси')
class TestTaxiOrderForm:
    """
    Тесты для проверки формы заказа такси
    """

    @allure.title('Открытие формы заказа со всеми 6 тарифами')
    @allure.description(
        'Проверка что при нажатии на кнопку Вызвать такси '
        'открывается форма заказа со всеми 6 тарифами, один из которых активный'
    )
    def test_taxi_order_form_with_all_tariffs(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Выбрать вид маршрута Быстрый'):
            main_page.click_route_type_fast()

        with allure.step('Нажать кнопку Вызвать такси'):
            main_page.click_call_taxi_button()

        with allure.step('Проверить, что форма заказа такси отображается'):
            assert main_page.is_taxi_order_form_visible(), \
                "Форма заказа такси должна отображаться после нажатия кнопки 'Вызвать такси'"

        with allure.step('Проверить, что отображается 6 тарифов'):
            tariffs_count = main_page.get_taxi_tariffs_count()
            assert tariffs_count == 6, \
                f"Должно отображаться 6 тарифов такси, найдено: {tariffs_count}"

        with allure.step('Проверить, что один из тарифов активный'):
            assert main_page.is_tariff_active(), \
                "Один из тарифов должен быть активным по умолчанию"


@allure.feature('Заказ тарифа Такси')
@allure.story('Сценарий заказа такси')
class TestTaxiOrderScenario:
    """
    Тест полного сценария заказа такси
    """

    @allure.title('Полный сценарий заказа такси с тарифом Рабочий')
    @allure.description(
        'Проверка полного сценария: выбор тарифа Рабочий, '
        'включение опции Столик для ноутбука, оформление заказа и проверка деталей'
    )
    def test_full_taxi_order_scenario(self, driver):
        with allure.step('Открыть главную страницу'):
            main_page = MainPage(driver)

        with allure.step('Ввести адрес начала маршрута: Хамовнический вал, 34'):
            main_page.enter_from_address(MainPage.ADDRESS_HAMOVNICHESKY)

        with allure.step('Ввести адрес конца маршрута: Зубовский бульвар, 37'):
            main_page.enter_to_address(MainPage.ADDRESS_ZUBOVSKY)

        with allure.step('Дождаться появления блока выбора маршрута'):
            main_page.wait_for_route_selection_block(timeout=10)

        with allure.step('Выбрать вид маршрута Быстрый'):
            main_page.click_route_type_fast()

        with allure.step('Нажать кнопку Вызвать такси'):
            main_page.click_call_taxi_button()

        with allure.step('Выбрать тариф Рабочий'):
            main_page.click_taxi_tariff_working()

        with allure.step('Сохранить стоимость поездки'):
            initial_cost = main_page.get_route_cost()

        with allure.step('Включить чекбокс Столик для ноутбука'):
            main_page.click_laptop_table_checkbox()

        with allure.step('Нажать кнопку Ввести номер и заказать'):
            main_page.click_enter_number_and_order_button()

        with allure.step('Проверить, что появилось окно ожидания машины'):
            assert main_page.is_waiting_window_visible(), \
                "Должно появиться окно ожидания машины"

        with allure.step('Проверить наличие заголовка Поиск машины'):
            assert main_page.is_waiting_title_visible(), \
                "Должен отображаться заголовок 'Поиск машины'"

        with allure.step('Проверить наличие таймера обратного отсчета'):
            assert main_page.is_waiting_timer_visible(), \
                "Должен отображаться таймер обратного отсчета"

        with allure.step('Дождаться окончания таймера поиска машины'):
            timer_completed = main_page.wait_for_timer_complete(timeout=60)
            assert timer_completed, "Таймер поиска машины должен завершиться"

        with allure.step('Проверить, что отображается окно совершенного заказа'):
            assert main_page.is_order_complete_window_visible(), \
                "Должно отображаться окно совершенного заказа"

        with allure.step('Проверить наличие заголовка с временем прибытия'):
            assert main_page.is_order_complete_title_visible(), \
                "Должен отображаться заголовок с временем прибытия"

        with allure.step('Проверить наличие номера автомобиля'):
            assert main_page.is_car_number_visible(), \
                "Должен отображаться номер автомобиля"

        with allure.step('Проверить наличие информации о водителе'):
            assert main_page.is_driver_info_visible(), \
                "Должна отображаться информация о водителе (имя, фото, рейтинг)"

        with allure.step('Нажать кнопку Детали'):
            main_page.click_details_button()

        with allure.step('Проверить, что окно деталей отображается'):
            assert main_page.is_details_window_visible(), \
                "Должно отображаться окно деталей заказа"

        with allure.step('Проверить стоимость в деталях'):
            details_cost = main_page.get_trip_cost_from_details()
            assert details_cost == initial_cost, \
                f"Стоимость в деталях ({details_cost}) должна совпадать с выбранной ({initial_cost})"

        with allure.step('Нажать кнопку Отмена'):
            main_page.click_cancel_button()

