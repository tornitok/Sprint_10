import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseObject:
    """Base class for all Page Objects containing shared methods."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Click on element: {locator}")
    def click(self, locator: tuple) -> None:
        """Wait for element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Enter text '{text}' into element: {locator}")
    def send_keys(self, locator: tuple, text: str) -> None:
        """Wait for element to be visible and enter text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Get text from element: {locator}")
    def get_text(self, locator: tuple) -> str:
        """Wait for element to be visible and return its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Get attribute '{attribute}' from element: {locator}")
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Wait for element to be present and return its attribute value."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    @allure.step("Check if element is visible: {locator}")
    def is_element_visible(self, locator: tuple, timeout: int = 10) -> bool:
        """Check if element is visible within timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Check if element is present: {locator}")
    def is_element_present(self, locator: tuple, timeout: int = 10) -> bool:
        """Check if element is present in DOM within timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Wait for element to be visible: {locator}")
    def wait_for_element_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Explicitly wait for element to be visible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Wait for element to be clickable: {locator}")
    def wait_for_element_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Explicitly wait for element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Hover over element: {locator}")
    def hover(self, locator: tuple) -> None:
        """Move mouse to element (hover action)."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Execute JavaScript: {script}")
    def execute_script(self, script: str, *args) -> any:
        """Execute JavaScript in the browser."""
        return self.driver.execute_script(script, *args)

    @allure.step("Wait for async operation using JavaScript setTimeout")
    def wait_for_async(self, milliseconds: int = 1000) -> None:
        """Wait for asynchronous behavior using JavaScript setTimeout."""
        self.driver.execute_script(f"""
            return new Promise(resolve => setTimeout(resolve, {milliseconds}));
        """)

    @allure.step("Scroll to element: {locator}")
    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll element into view."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Get current URL")
    def get_current_url(self) -> str:
        """Return current page URL."""
        return self.driver.current_url

    @allure.step("Find element: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        """Find and return element."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Find all elements: {locator}")
    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Find and return all matching elements."""
        return self.driver.find_elements(*locator)

    @allure.step("Wait for element to disappear: {locator}")
    def wait_for_element_invisible(self, locator: tuple, timeout: int = 10) -> bool:
        """Wait for element to become invisible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
