import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class Page04(BasePage):

    ELEMENTS_CARD = (By.XPATH, "//h5[normalize-space()='Elements']")
    BUTTONS_MENU = (By.XPATH, "//span[normalize-space()='Buttons']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_buttons(self):
        # Step 1: Elements card click karo
        elements_card = self.wait.until(EC.presence_of_element_located(self.ELEMENTS_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_card)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", elements_card)

        # Step 2: Left sidebar mein "Buttons" click karo
        buttons_menu = self.wait.until(EC.presence_of_element_located(self.BUTTONS_MENU))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons_menu)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", buttons_menu)