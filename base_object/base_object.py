from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import urllib.parse
import re


class BaseObject:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _is_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def _is_not_clickable(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until_not(ec.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def _is_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator))

    def _are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def _is_not_visible(self, locator: tuple[str, str]):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def _url_contains(self, text: str) -> bool:
        return self.wait.until(lambda d: text in d.current_url)

    @staticmethod
    def js_click(element: WebElement) -> None:
        """JavaScript клик по элементу."""
        element.parent.execute_script("arguments[0].click();", element)

    def click(self, locator: tuple[str, str], ensure_clickable=True) -> None:
        element = self._is_clickable(locator) if ensure_clickable else self._is_present(locator)
        try:
            element.click()
        except Exception:
            self.js_click(element)

    def send_keys(self, locator: tuple[str, str], value: str, ensure_visible=True) -> None:
        element = self._is_visible(locator) if ensure_visible else self._is_present(locator)
        element.send_keys(value)

    def get_current_url(self, wait_locator: tuple[str, str]) -> str:
        self._is_not_visible(wait_locator)
        return urllib.parse.unquote(self.driver.current_url)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self._is_visible(locator).text

    def get_elements_count(self, locator: tuple[str, str], min_count: int | None = None) -> int:
        if min_count is None:
            elements = self._are_present(locator)
        else:
            self.wait.until(lambda d: len(d.find_elements(*locator)) >= min_count)
            elements = self.driver.find_elements(*locator)
        return len(elements)

    @staticmethod
    def normalize_text(text: str, prefer_email=False, prefer_first_line=False) -> str:
        """Очистка текста: убрать переносы, извлечь email или первую строку."""
        if not text:
            return ""
        text = text.strip()
        if "\n" in text:
            parts = [p.strip() for p in text.split("\n") if p.strip()]
            if prefer_email:
                for p in reversed(parts):
                    if "@" in p and "." in p:
                        return p
            if prefer_first_line:
                return parts[0]
            return " ".join(parts)
        if prefer_email:
            m = re.search(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", text)
            return m.group(0) if m else text
        return text

    def clean_field(self, locator: tuple[str, str]) -> None:
        """Очистка текстового поля."""
        element = self._is_visible(locator)
        element.clear()

    def hover(self, locator: tuple[str, str]) -> None:
        """
        Наведение курсора на элемент.
        Использует ActionChains для эмуляции hover действия.

        :param locator: кортеж (метод поиска, значение)
        """
        element = self._is_visible(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def hover_and_click(self, hover_locator: tuple[str, str], click_locator: tuple[str, str]) -> None:
        """
        Наведение курсора на элемент и клик по другому элементу.
        Полезно для работы с выпадающими меню.

        :param hover_locator: локатор элемента для наведения
        :param click_locator: локатор элемента для клика
        """
        hover_element = self._is_visible(hover_locator)
        ActionChains(self.driver).move_to_element(hover_element).perform()
        self.click(click_locator)


    @staticmethod
    def is_sorted_ascending(values: list) -> bool:
        normalized = [v.lower() for v in values]
        return normalized == sorted(normalized)

    @staticmethod
    def is_sorted_descending(values: list) -> bool:
        normalized = [v.lower() for v in values]
        return normalized == sorted(normalized, reverse=True)

    def wait_for_condition(self, condition, timeout: int = 10) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(condition)
        return True

    def wait_for_elements_count(self, locator: tuple[str, str], min_count: int, timeout: int = 10) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: len(d.find_elements(*locator)) >= min_count)
        return True

