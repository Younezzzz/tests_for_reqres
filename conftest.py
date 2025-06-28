import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/"

@pytest.fixture(scope="session")
def api_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def headers():
    return {"x-api-key":"reqres-free-v1"}