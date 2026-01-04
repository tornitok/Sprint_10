"""
Скрипт для проверки и определения правильных локаторов на сайте EZ Route.
Запускает браузер и позволяет вручную изучить элементы страницы.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def find_locators():
    """
    Функция для поиска правильных локаторов элементов на странице
    """
    # Настройка Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Открываем сайт
        print("Открываем сайт...")
        driver.get('https://ez-route.stand.praktikum-services.ru')
        time.sleep(3)

        print("\nСтраница загружена. Начинаем поиск элементов...\n")

        # Список возможных локаторов для полей ввода "Откуда"
        from_field_locators = [
            ("ID", "address-from"),
            ("NAME", "from"),
            ("CSS", "input[placeholder*='Откуда']"),
            ("CSS", "input[placeholder*='откуда']"),
            ("CSS", "input[name*='from']"),
            ("CSS", "input[id*='from']"),
            ("XPATH", "//input[contains(@placeholder, 'Откуда')]"),
            ("XPATH", "//input[contains(@placeholder, 'откуда')]"),
        ]

        print("Поиск поля 'Откуда':")
        for method, locator in from_field_locators:
            try:
                if method == "ID":
                    element = driver.find_element(By.ID, locator)
                elif method == "NAME":
                    element = driver.find_element(By.NAME, locator)
                elif method == "CSS":
                    element = driver.find_element(By.CSS_SELECTOR, locator)
                elif method == "XPATH":
                    element = driver.find_element(By.XPATH, locator)

                print(f"  ✓ Найдено: {method} = '{locator}'")
                print(f"    Tag: {element.tag_name}, Visible: {element.is_displayed()}")
            except:
                pass

        # Список возможных локаторов для полей ввода "Куда"
        to_field_locators = [
            ("ID", "address-to"),
            ("NAME", "to"),
            ("CSS", "input[placeholder*='Куда']"),
            ("CSS", "input[placeholder*='куда']"),
            ("CSS", "input[name*='to']"),
            ("CSS", "input[id*='to']"),
            ("XPATH", "//input[contains(@placeholder, 'Куда')]"),
            ("XPATH", "//input[contains(@placeholder, 'куда')]"),
        ]

        print("\nПоиск поля 'Куда':")
        for method, locator in to_field_locators:
            try:
                if method == "ID":
                    element = driver.find_element(By.ID, locator)
                elif method == "NAME":
                    element = driver.find_element(By.NAME, locator)
                elif method == "CSS":
                    element = driver.find_element(By.CSS_SELECTOR, locator)
                elif method == "XPATH":
                    element = driver.find_element(By.XPATH, locator)

                print(f"  ✓ Найдено: {method} = '{locator}'")
                print(f"    Tag: {element.tag_name}, Visible: {element.is_displayed()}")
            except:
                pass

        # Поиск всех input элементов для анализа
        print("\n" + "="*60)
        print("Все input элементы на странице:")
        print("="*60)
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for i, inp in enumerate(inputs, 1):
            print(f"\nInput #{i}:")
            print(f"  ID: {inp.get_attribute('id')}")
            print(f"  Name: {inp.get_attribute('name')}")
            print(f"  Placeholder: {inp.get_attribute('placeholder')}")
            print(f"  Class: {inp.get_attribute('class')}")
            print(f"  Type: {inp.get_attribute('type')}")

        # Поиск кнопок
        print("\n" + "="*60)
        print("Все кнопки на странице:")
        print("="*60)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, btn in enumerate(buttons, 1):
            print(f"\nButton #{i}:")
            print(f"  ID: {btn.get_attribute('id')}")
            print(f"  Text: {btn.text}")
            print(f"  Class: {btn.get_attribute('class')}")

        # Поиск карты
        print("\n" + "="*60)
        print("Поиск карты:")
        print("="*60)
        map_locators = [
            ("ID", "map"),
            ("CLASS", "map"),
            ("CSS", "[class*='map']"),
            ("CSS", "[id*='map']"),
        ]

        for method, locator in map_locators:
            try:
                if method == "ID":
                    element = driver.find_element(By.ID, locator)
                elif method == "CLASS":
                    element = driver.find_element(By.CLASS_NAME, locator)
                elif method == "CSS":
                    element = driver.find_element(By.CSS_SELECTOR, locator)

                print(f"  ✓ Найдено: {method} = '{locator}'")
            except:
                pass

        print("\n" + "="*60)
        print("Браузер останется открытым на 30 секунд для изучения.")
        print("Используйте DevTools (F12) для дополнительного анализа.")
        print("="*60)

        time.sleep(30)

    finally:
        driver.quit()
        print("\nБраузер закрыт.")


if __name__ == "__main__":
    find_locators()

