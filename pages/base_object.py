"""Базовый класс для всех Page Objects."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseObject:
    """Базовый класс для всех Page Objects с общими методами."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: tuple) -> None:
        """Ожидание кликабельности элемента и клик."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def send_keys(self, locator: tuple, text: str) -> None:
        """Ожидание видимости элемента и ввод текста."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator: tuple) -> str:
        """Ожидание видимости элемента и возврат его текста."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Получение атрибута '{attribute}' из элемента: {locator}")
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Ожидание присутствия элемента и возврат значения атрибута."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    @allure.step("Проверка видимости элемента: {locator}")
    def is_element_visible(self, locator: tuple, timeout: int = 10) -> bool:
        """Проверка видимости элемента в течение таймаута."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Проверка присутствия элемента: {locator}")
    def is_element_present(self, locator: tuple, timeout: int = 10) -> bool:
        """Проверка присутствия элемента в DOM в течение таймаута."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Явное ожидание видимости элемента."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_for_element_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Явное ожидание кликабельности элемента."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Наведение на элемент: {locator}")
    def hover(self, locator: tuple) -> None:
        """Наведение курсора на элемент."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Выполнение JavaScript: {script}")
    def execute_script(self, script: str, *args) -> any:
        """Выполнение JavaScript в браузере."""
        return self.driver.execute_script(script, *args)

    @allure.step("Ожидание асинхронной операции через JavaScript setTimeout")
    def wait_for_async(self, milliseconds: int = 1000) -> None:
        """Ожидание асинхронного поведения через JavaScript setTimeout."""
        self.driver.execute_script(f"""
            return new Promise(resolve => setTimeout(resolve, {milliseconds}));
        """)

    @allure.step("Прокрутка к элементу: {locator}")
    def scroll_to_element(self, locator: tuple) -> None:
        """Прокрутка страницы до элемента."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        """Возврат URL текущей страницы."""
        return self.driver.current_url

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        """Поиск и возврат элемента."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов: {locator}")
    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Поиск и возврат всех соответствующих элементов."""
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_element_invisible(self, locator: tuple, timeout: int = 10) -> bool:
        """Ожидание невидимости элемента."""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
