import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import URL


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless=new")  # при необходимости
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(
        ChromeDriverManager().install()
    )

    browser = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    browser.get(URL.BASE_URL)
    browser.implicitly_wait(10)

    yield browser

    browser.quit()
