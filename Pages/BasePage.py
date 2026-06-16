import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Common helper — koi bhi page use kar sakta hai
    def click_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_title(self):
        return self.driver.title