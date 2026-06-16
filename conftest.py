import pytest
from Utilities.ReadConfig import ReadConfig
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")





@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "--headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "edge" :
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(ReadConfig().get_application_url())
    expected_title = "demosite"
    actual_title = driver.title
    assert actual_title == expected_title
    request.cls.driver = driver
    yield driver
    driver.quit()