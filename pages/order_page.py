"""Page Object для страницы заказа такси."""

import allure
from selenium.webdriver.common.by import By
from pages.base_object import BaseObject
from locators.order_page_locators import OrderPageLocators


class OrderPage(BaseObject):
    """Page Object для страницы заказа такси."""

    @allure.step("Проверка отображения формы заказа")
    def is_order_form_displayed(self) -> bool:
        """Проверка видимости формы заказа."""
        return self.is_element_visible(OrderPageLocators.ORDER_FORM)

    @allure.step("Ожидание отображения формы заказа")
    def wait_for_order_form_displayed(self, timeout: int = 10) -> None:
        """Явное ожидание видимости формы заказа."""
        self.wait_for_element_visible(OrderPageLocators.ORDER_FORM, timeout)

    @allure.step("Выбор тарифа Эконом")
    def select_economy_tariff(self) -> None:
        """Выбор тарифа Эконом."""
        self.click(OrderPageLocators.ECONOMY_TARIFF)

    @allure.step("Выбор тарифа Комфорт")
    def select_comfort_tariff(self) -> None:
        """Выбор тарифа Комфорт."""
        self.click(OrderPageLocators.COMFORT_TARIFF)

    @allure.step("Выбор тарифа Бизнес")
    def select_business_tariff(self) -> None:
        """Выбор тарифа Бизнес."""
        self.click(OrderPageLocators.BUSINESS_TARIFF)

    @allure.step("Ввод номера телефона: {phone}")
    def enter_phone(self, phone: str) -> None:
        """Ввод номера телефона в форму заказа."""
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Ввод комментария: {comment}")
    def enter_comment(self, comment: str) -> None:
        """Ввод комментария к заказу."""
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Клик по кнопке подтверждения заказа")
    def click_confirm_order(self) -> None:
        """Клик по кнопке подтверждения заказа."""
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получение стоимости заказа")
    def get_order_price(self) -> str:
        """Получение отображаемой стоимости заказа."""
        return self.get_text(OrderPageLocators.ORDER_PRICE)

    @allure.step("Выбор оплаты картой")
    def select_card_payment(self) -> None:
        """Выбор способа оплаты картой."""
        self.click(OrderPageLocators.CARD_PAYMENT)

    @allure.step("Выбор оплаты наличными")
    def select_cash_payment(self) -> None:
        """Выбор способа оплаты наличными."""
        self.click(OrderPageLocators.CASH_PAYMENT)

    @allure.step("Наведение на селектор тарифов")
    def hover_over_tariff_selector(self) -> None:
        """Наведение на селектор тарифов."""
        self.hover(OrderPageLocators.TARIFF_SELECTOR)

    # Методы работы с тарифами такси
    @allure.step("Выбор тарифа Рабочий")
    def select_business_fare(self) -> None:
        """Выбор тарифа Рабочий."""
        self.click(OrderPageLocators.BUSINESS_FARE)

    @allure.step("Выбор тарифа Сонный")
    def select_sleepy_fare(self) -> None:
        """Выбор тарифа Сонный."""
        self.click(OrderPageLocators.SLEEPY_FARE)

    @allure.step("Выбор тарифа Отпускной")
    def select_vacation_fare(self) -> None:
        """Выбор тарифа Отпускной."""
        self.click(OrderPageLocators.VACATION_FARE)

    @allure.step("Выбор тарифа Разговорчивый")
    def select_talkative_fare(self) -> None:
        """Выбор тарифа Разговорчивый."""
        self.click(OrderPageLocators.TALKATIVE_FARE)

    @allure.step("Выбор тарифа Утешительный")
    def select_comforting_fare(self) -> None:
        """Выбор тарифа Утешительный."""
        self.click(OrderPageLocators.COMFORTING_FARE)

    @allure.step("Выбор тарифа Глянцевый")
    def select_glossy_fare(self) -> None:
        """Выбор тарифа Глянцевый."""
        self.click(OrderPageLocators.GLOSSY_FARE)

    @allure.step("Получение количества отображаемых тарифов")
    def get_fares_count(self) -> int:
        """Получение количества отображаемых тарифов такси."""
        if self.is_element_visible(OrderPageLocators.ALL_FARES, timeout=5):
            elements = self.find_elements(OrderPageLocators.ALL_FARES)
            return len(elements)
        return 0

    @allure.step("Проверка активности ровно одного тарифа")
    def is_one_fare_active(self) -> bool:
        """Проверка что ровно один тариф выбран по умолчанию."""
        elements = self.find_elements(OrderPageLocators.ACTIVE_FARE)
        return len(elements) == 1

    @allure.step("Получение названия активного тарифа")
    def get_active_fare_name(self) -> str:
        """Получение названия текущего активного тарифа."""
        element = self.find_element(OrderPageLocators.ACTIVE_FARE)
        return element.text

    @allure.step("Проверка видимости тарифа: {fare_name}")
    def is_fare_visible(self, fare_name: str) -> bool:
        """Проверка видимости конкретного тарифа.

        Поддерживает как тарифы Такси, так и тарифы Драйв (tcard с русским текстом).
        """
        # Маппинг названий тарифов
        fare_map = {
            # Тарифы Драйв (русский UI)
            "повседневный": "Повседневный",
            "походный": "Походный",
            "роскошный": "Роскошный",
            # Тарифы Такси (русский UI)
            "рабочий": "Рабочий",
            "сонный": "Сонный",
            "отпускной": "Отпускной",
            "разговорчивый": "Разговорчивый",
            "утешительный": "Утешительный",
            "глянцевый": "Глянцевый"
        }

        fare_lower = fare_name.lower()

        # Поиск тарифа по русскому названию в tcard
        if fare_lower in fare_map:
            russian_name = fare_map[fare_lower]
            locator = (By.XPATH, OrderPageLocators.TCARD_BY_NAME_TEMPLATE.format(russian_name))
            return self.is_element_visible(locator, timeout=5)

        # Fallback: поиск как есть
        locator = (By.XPATH, OrderPageLocators.TCARD_BY_NAME_TEMPLATE.format(fare_name))
        return self.is_element_visible(locator, timeout=5)

    # Методы работы с всплывающими подсказками тарифов
    @allure.step("Наведение на иконку информации тарифа: {fare_name}")
    def hover_fare_info_icon(self, fare_name: str) -> None:
        """Показать всплывающую подсказку для указанного тарифа.

        Для тарифов Такси контент подсказки встроен в HTML tcard.
        Используем JavaScript для показа подсказки добавлением класса 'show'.
        Для тарифов Драйв клик по tcard показывает описание в превью.
        """
        # Маппинг названий тарифов
        fare_map = {
            # Тарифы Драйв
            "повседневный": "Повседневный",
            "походный": "Походный",
            "роскошный": "Роскошный",
            # Тарифы Такси
            "рабочий": "Рабочий",
            "сонный": "Сонный",
            "отпускной": "Отпускной",
            "разговорчивый": "Разговорчивый",
            "утешительный": "Утешительный",
            "глянцевый": "Глянцевый"
        }

        fare_lower = fare_name.lower()
        drive_fares = ["повседневный", "походный", "роскошный"]

        if fare_lower in fare_map:
            russian_name = fare_map[fare_lower]

            if fare_lower in drive_fares:
                # Для тарифов Драйв клик по tcard показывает превью
                locator = (By.XPATH, OrderPageLocators.TCARD_PARENT_BY_NAME_TEMPLATE.format(russian_name))
                self.click(locator)
            else:
                # Для тарифов Такси используем JavaScript для показа подсказки
                script = f"""
                    const tcards = document.querySelectorAll('.tcard');
                    for (const tcard of tcards) {{
                        const title = tcard.querySelector('.tcard-title');
                        if (title && title.textContent.includes('{russian_name}')) {{
                            const tooltip = tcard.querySelector('[class*="react_component_tooltip"]');
                            if (tooltip) {{
                                tooltip.classList.add('show');
                                tooltip.style.opacity = '1';
                                tooltip.style.visibility = 'visible';
                            }}
                            break;
                        }}
                    }}
                """
                self.execute_script(script)
        else:
            # Fallback: поиск по названию как есть
            locator = (By.XPATH, OrderPageLocators.TCARD_PARENT_BY_NAME_TEMPLATE.format(fare_name))
            self.click(locator)

    @allure.step("Получение текста подсказки")
    def get_tooltip_text(self) -> str:
        """Получение текста описания из подсказки или превью.

        Для тарифов Такси возвращает текст из React tooltip (.i-dPrefix).
        Для тарифов Драйв возвращает описание из drive-preview-prefix.
        """
        # Сначала пробуем drive-preview-prefix (для тарифов Драйв)
        if self.is_element_visible(OrderPageLocators.DRIVE_PREVIEW_PREFIX, timeout=2):
            return self.get_text(OrderPageLocators.DRIVE_PREVIEW_PREFIX)

        # Пробуем получить текст подсказки через JavaScript (для тарифов Такси)
        result = self.execute_script("""
            const tooltip = document.querySelector('[class*="react_component_tooltip"].show .i-dPrefix');
            if (tooltip) return tooltip.textContent;
            
            // Пробуем все видимые подсказки
            const allTooltips = document.querySelectorAll('.i-dPrefix');
            for (const t of allTooltips) {
                if (t.textContent && t.textContent.trim()) {
                    return t.textContent;
                }
            }
            return null;
        """)
        if result:
            return result

        # Пробуем React tooltip (для тарифов Такси) - появляется при наведении на .tcard-i
        if self.is_element_visible(OrderPageLocators.TAXI_TOOLTIP_TEXT, timeout=2):
            return self.get_text(OrderPageLocators.TAXI_TOOLTIP_TEXT)


        # Пробуем получить описание из активного tcard
        if self.is_element_visible(OrderPageLocators.ACTIVE_TCARD_DESC, timeout=2):
            return self.get_text(OrderPageLocators.ACTIVE_TCARD_DESC)

        # Fallback к обычной подсказке
        return self.get_text(OrderPageLocators.FARE_TOOLTIP)

    @allure.step("Получение текста подсказки для конкретного тарифа: {fare_name}")
    def get_fare_tooltip_text(self, fare_name: str) -> str:
        """Получение текста описания для конкретного тарифа из его подсказки.

        Args:
            fare_name: Название тарифа (например, 'Рабочий', 'Сонный')

        Returns:
            Текст описания подсказки для тарифа.
        """
        # Маппинг названий тарифов
        fare_map = {
            "рабочий": "Рабочий",
            "сонный": "Сонный",
            "отпускной": "Отпускной",
            "разговорчивый": "Разговорчивый",
            "утешительный": "Утешительный",
            "глянцевый": "Глянцевый"
        }

        fare_lower = fare_name.lower()
        russian_name = fare_map.get(fare_lower, fare_name)

        # Используем JavaScript для получения текста подсказки конкретного тарифа
        result = self.execute_script(f"""
            const tcards = document.querySelectorAll('.tcard');
            for (const tcard of tcards) {{
                const title = tcard.querySelector('.tcard-title');
                if (title && title.textContent.includes('{russian_name}')) {{
                    const desc = tcard.querySelector('.i-dPrefix');
                    if (desc) return desc.textContent;
                }}
            }}
            return null;
        """)
        return result if result else ""

    @allure.step("Проверка отображения подсказки")
    def is_tooltip_displayed(self) -> bool:
        """Проверка видимости подсказки или превью Драйв."""
        return (self.is_element_visible(OrderPageLocators.DRIVE_PREVIEW_PREFIX, timeout=2) or
                self.is_element_visible(OrderPageLocators.FARE_TOOLTIP, timeout=2))

    # Методы работы с полями формы заказа
    @allure.step("Проверка отображения поля телефона")
    def is_phone_field_displayed(self) -> bool:
        """Проверка видимости или присутствия поля номера телефона."""
        return (self.is_element_visible(OrderPageLocators.PHONE_INPUT, timeout=3) or
                self.is_element_present(OrderPageLocators.PHONE_INPUT, timeout=3) or
                self.is_element_visible(OrderPageLocators.PHONE_FIELD, timeout=3))

    @allure.step("Проверка отображения поля способа оплаты")
    def is_payment_method_field_displayed(self) -> bool:
        """Проверка видимости или присутствия поля способа оплаты."""
        return (self.is_element_visible(OrderPageLocators.PAYMENT_METHOD_SELECTOR, timeout=3) or
                self.is_element_present(OrderPageLocators.PAYMENT_METHOD_SELECTOR, timeout=3) or
                self.is_element_visible(OrderPageLocators.PAYMENT_METHOD_FIELD, timeout=3))

    @allure.step("Проверка отображения поля комментария")
    def is_comment_field_displayed(self) -> bool:
        """Проверка видимости поля комментария для водителя."""
        return (self.is_element_visible(OrderPageLocators.COMMENT_INPUT, timeout=3) or
                self.is_element_visible(OrderPageLocators.COMMENT_FIELD, timeout=3))

    @allure.step("Проверка отображения поля требований к заказу")
    def is_requirements_field_displayed(self) -> bool:
        """Проверка видимости поля требований к заказу."""
        return self.is_element_visible(OrderPageLocators.REQUIREMENTS_FIELD, timeout=3)

    @allure.step("Раскрытие секции Требования к заказу")
    def expand_requirements_section(self) -> None:
        """Раскрытие секции Требования к заказу если она закрыта."""
        self.scroll_to_element(OrderPageLocators.REQUIREMENTS_HEADER)
        self.click(OrderPageLocators.REQUIREMENTS_HEADER)

    @allure.step("Проверка выбора Столик для ноутбука")
    def is_laptop_table_selected(self) -> bool:
        """Проверка выбора чекбокса Столик для ноутбука."""
        element = self.find_element(OrderPageLocators.LAPTOP_TABLE_CHECKBOX)
        return element.is_selected()

    # Методы действий с заказом
    @allure.step("Клик по кнопке 'Ввести номер и заказать'")
    def click_enter_number_and_order(self) -> None:
        """Клик по кнопке Ввести номер и заказать."""
        self.click(OrderPageLocators.ENTER_NUMBER_ORDER_BUTTON)

    @allure.step("Клик по кнопке Отменить")
    def click_cancel(self) -> None:
        """Клик по кнопке Отменить."""
        self.click(OrderPageLocators.CANCEL_BUTTON)

    @allure.step("Клик по кнопке Детали")
    def click_details(self) -> None:
        """Клик по кнопке Детали."""
        self.click(OrderPageLocators.DETAILS_BUTTON)

    # Методы работы с окном поиска машины
    @allure.step("Проверка отображения окна поиска машины")
    def is_car_search_window_displayed(self) -> bool:
        """Проверка видимости окна поиска машины."""
        return self.is_element_visible(OrderPageLocators.CAR_SEARCH_WINDOW)

    @allure.step("Ожидание отображения окна поиска машины")
    def wait_for_car_search_window_displayed(self, timeout: int = 30) -> None:
        """Ожидание появления окна поиска машины."""
        self.wait_for_element_visible(OrderPageLocators.CAR_SEARCH_WINDOW, timeout)

    @allure.step("Получение заголовка окна поиска машины")
    def get_car_search_title(self) -> str:
        """Получение заголовка окна поиска машины."""
        return self.get_text(OrderPageLocators.CAR_SEARCH_TITLE)

    @allure.step("Проверка отображения таймера поиска")
    def is_search_timer_displayed(self) -> bool:
        """Проверка видимости таймера обратного отсчета."""
        return self.is_element_visible(OrderPageLocators.CAR_SEARCH_TIMER)

    @allure.step("Ожидание завершения поиска машины")
    def wait_for_search_complete(self, timeout: int = 60) -> None:
        """Ожидание завершения таймера поиска машины и появления окна совершенного заказа."""
        # Ждём исчезновения заголовка "Поиск машины"
        self.wait_for_element_invisible(OrderPageLocators.SEARCHING_CAR_TITLE, timeout)

    @allure.step("Ожидание появления окна совершенного заказа")
    def wait_for_completed_order_displayed(self, timeout: int = 10) -> None:
        """Ожидание появления окна совершенного заказа."""
        self.wait_for_element_invisible(OrderPageLocators.SEARCHING_CAR_TITLE, timeout)

    # Методы работы с окном совершенного заказа
    @allure.step("Проверка отображения окна совершенного заказа")
    def is_completed_order_displayed(self) -> bool:
        """Проверка видимости окна совершенного заказа."""
        return self.is_element_visible(OrderPageLocators.ORDER_TITLE)

    @allure.step("Получение заголовка заказа")
    def get_order_title(self) -> str:
        """Получение заголовка заказа (например, 'N мин. и приедет')."""
        return self.get_text(OrderPageLocators.ORDER_TITLE)

    @allure.step("Проверка отображения номера машины")
    def is_car_number_displayed(self) -> bool:
        """Проверка видимости номера машины."""
        return self.is_element_visible(OrderPageLocators.CAR_NUMBER)

    @allure.step("Получение номера машины")
    def get_car_number(self) -> str:
        """Получение номера машины."""
        return self.get_text(OrderPageLocators.CAR_NUMBER)

    @allure.step("Проверка отображения изображения тарифа")
    def is_fare_image_displayed(self) -> bool:
        """Проверка видимости изображения тарифа."""
        return self.is_element_visible(OrderPageLocators.FARE_IMAGE)

    # Методы работы с информацией о водителе
    @allure.step("Проверка отображения информации о водителе")
    def is_driver_info_displayed(self) -> bool:
        """Проверка видимости блока информации о водителе."""
        return self.is_element_visible(OrderPageLocators.DRIVER_INFO_BLOCK)

    @allure.step("Получение имени водителя")
    def get_driver_name(self) -> str:
        """Получение имени водителя."""
        return self.get_text(OrderPageLocators.DRIVER_NAME)

    @allure.step("Проверка отображения фото водителя")
    def is_driver_photo_displayed(self) -> bool:
        """Проверка видимости фото водителя."""
        return self.is_element_visible(OrderPageLocators.DRIVER_PHOTO)

    @allure.step("Получение рейтинга водителя")
    def get_driver_rating(self) -> str:
        """Получение рейтинга водителя."""
        return self.get_text(OrderPageLocators.DRIVER_RATING)

    # Методы работы с деталями заказа
    @allure.step("Проверка отображения окна деталей заказа")
    def is_order_details_displayed(self) -> bool:
        """Проверка видимости окна деталей заказа."""
        return self.is_element_visible(OrderPageLocators.ORDER_DETAILS_WINDOW)

    @allure.step("Получение адреса подачи из деталей")
    def get_pickup_address(self) -> str:
        """Получение адреса подачи из деталей заказа."""
        return self.get_text(OrderPageLocators.PICKUP_ADDRESS)

    @allure.step("Получение адреса назначения из деталей")
    def get_destination_address(self) -> str:
        """Получение адреса назначения из деталей заказа."""
        return self.get_text(OrderPageLocators.DESTINATION_ADDRESS)

    @allure.step("Получение способа оплаты из деталей")
    def get_payment_method_display(self) -> str:
        """Получение способа оплаты из деталей заказа."""
        return self.get_text(OrderPageLocators.PAYMENT_METHOD_DISPLAY)

    @allure.step("Получение стоимости поездки из деталей")
    def get_trip_cost(self) -> str:
        """Получение стоимости поездки из деталей заказа."""
        return self.get_text(OrderPageLocators.TRIP_COST)

    @allure.step("Проверка закрытия окна заказа")
    def is_order_window_closed(self) -> bool:
        """Проверка закрытия окна заказа."""
        return not self.is_element_visible(OrderPageLocators.COMPLETED_ORDER_WINDOW, timeout=3)

    # Методы работы с заказом Драйв
    @allure.step("Проверка отображения формы заказа Драйв")
    def is_drive_order_form_displayed(self) -> bool:
        """Проверка видимости формы заказа Драйв."""
        return self.is_element_visible(OrderPageLocators.DRIVE_ORDER_FORM)

    @allure.step("Выбор тарифа Повседневный")
    def select_everyday_fare(self) -> None:
        """Выбор тарифа Повседневный."""
        self.click(OrderPageLocators.EVERYDAY_FARE)

    @allure.step("Выбор тарифа Походный")
    def select_outdoor_fare(self) -> None:
        """Выбор тарифа Походный."""
        self.click(OrderPageLocators.OUTDOOR_FARE)

    @allure.step("Выбор тарифа Роскошный")
    def select_luxury_fare(self) -> None:
        """Выбор тарифа Роскошный."""
        self.click(OrderPageLocators.LUXURY_FARE)

    # Методы работы с правами водителя
    @allure.step("Клик по кнопке 'Добавить права'")
    def click_add_license_button(self) -> None:
        """Клик по кнопке 'Добавить права' для открытия окна ввода прав."""
        self.click(OrderPageLocators.ADD_LICENSE_BUTTON_NP)

    @allure.step("Проверка отображения окна добавления прав")
    def is_license_window_displayed(self) -> bool:
        """Проверка видимости окна добавления водительских прав."""
        return self.is_element_visible(OrderPageLocators.FIRST_NAME_INPUT)

    @allure.step("Ввод имени: {first_name}")
    def enter_first_name(self, first_name: str) -> None:
        """Ввод имени в форму прав."""
        self.click(OrderPageLocators.FIRST_NAME_INPUT)
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step("Ввод фамилии: {last_name}")
    def enter_last_name(self, last_name: str) -> None:
        """Ввод фамилии в форму прав."""
        self.click(OrderPageLocators.LAST_NAME_INPUT)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Ввод даты рождения: {dob}")
    def enter_date_of_birth(self, dob: str) -> None:
        """Ввод даты рождения в форму прав."""
        self.click(OrderPageLocators.DATE_OF_BIRTH_INPUT)
        self.send_keys(OrderPageLocators.DATE_OF_BIRTH_INPUT, dob)

    @allure.step("Ввод номера прав: {license_num}")
    def enter_license_number(self, license_num: str) -> None:
        """Ввод номера прав в форму."""
        self.click(OrderPageLocators.LICENSE_NUMBER_INPUT)
        self.send_keys(OrderPageLocators.LICENSE_NUMBER_INPUT, license_num)
        self.click(OrderPageLocators.DATE_OF_BIRTH_INPUT)

    @allure.step("Клик по кнопке Добавить")
    def click_add_license(self) -> None:
        """Клик по кнопке Добавить в форме прав."""
        self.click(OrderPageLocators.ADD_LICENSE_BUTTON)

    @allure.step("Клик по кнопке Принято в окне подтверждения")
    def click_license_confirmation(self) -> None:
        """Клик по кнопке Принято в окне подтверждения после добавления прав."""
        self.click(OrderPageLocators.LICENSE_CONFIRMATION_BUTTON)

    @allure.step("Проверка отображения окна подтверждения прав")
    def is_license_confirmation_displayed(self) -> bool:
        """Проверка видимости окна подтверждения после добавления прав."""
        return self.is_element_visible(OrderPageLocators.LICENSE_CONFIRMATION_WINDOW)

    @allure.step("Клик по кнопке Отмена в форме прав")
    def click_cancel_license(self) -> None:
        """Клик по кнопке Отмена в форме прав."""
        self.click(OrderPageLocators.CANCEL_LICENSE_BUTTON)

    @allure.step("Проверка отображения поля имени")
    def is_first_name_field_displayed(self) -> bool:
        """Проверка видимости поля имени в форме прав."""
        return self.is_element_visible(OrderPageLocators.FIRST_NAME_INPUT)

    @allure.step("Проверка отображения поля фамилии")
    def is_last_name_field_displayed(self) -> bool:
        """Проверка видимости поля фамилии в форме прав."""
        return self.is_element_visible(OrderPageLocators.LAST_NAME_INPUT)

    @allure.step("Проверка отображения поля даты рождения")
    def is_date_of_birth_field_displayed(self) -> bool:
        """Проверка видимости поля даты рождения в форме прав."""
        return self.is_element_visible(OrderPageLocators.DATE_OF_BIRTH_INPUT)

    @allure.step("Проверка отображения поля номера прав")
    def is_license_number_field_displayed(self) -> bool:
        """Проверка видимости поля номера прав в форме."""
        return self.is_element_visible(OrderPageLocators.LICENSE_NUMBER_INPUT)

    # Методы работы с окном совершенного заказа Драйв
    @allure.step("Проверка отображения окна заказа Драйв")
    def is_drive_order_window_displayed(self) -> bool:
        """Проверка видимости окна совершенного заказа Драйв."""
        return self.is_element_visible(OrderPageLocators.DRIVE_ORDER_WINDOW)

    @allure.step("Проверка отображения таймера бесплатного ожидания")
    def is_free_waiting_timer_displayed(self) -> bool:
        """Проверка видимости таймера бесплатного ожидания."""
        return self.is_element_visible(OrderPageLocators.FREE_WAITING_TIMER)

    @allure.step("Получение адреса местоположения машины")
    def get_car_location_address(self) -> str:
        """Получение адреса местоположения машины (Откуда)."""
        return self.get_text(OrderPageLocators.CAR_LOCATION_ADDRESS)
