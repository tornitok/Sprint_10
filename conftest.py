import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://ez-route.stand.praktikum-services.ru/"


@pytest.fixture
def driver():
    """Initialize Chrome WebDriver with options."""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()


@pytest.fixture
def open_main_page(driver):
    """Open the main page of the application."""
    driver.get(BASE_URL)
    return driver
