import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page03:
    element_btn = (By.XPATH,"//h5[normalize-space()='Elements']")
    checkbox_btn = (By.XPATH,"//span[normalize-space()='Check Box']")
    home_btn = (By.XPATH,"//span[@aria-label='Select Home']")
    home_list_btn = (By.XPATH,"//span[@class='rc-tree-switcher rc-tree-switcher_close']")
    dekstop_list_btn = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/span[2]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click_element(self):
        self.wait.until(EC.element_to_be_clickable(self.element_btn)).click()

    def click_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.checkbox_btn)).click()

    def click_home(self):
        self.wait.until(EC.element_to_be_clickable(self.home_btn)).click()

    def click_homelist(self):
        self.wait.until(EC.element_to_be_clickable(self.home_list_btn)).click()

    def click_desktop(self):
        self.wait.until(EC.element_to_be_clickable(self.dekstop_list_btn)).click()



