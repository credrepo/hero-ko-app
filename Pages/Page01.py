import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page01:
    ele_btn_clk = (By.XPATH, "//h5[normalize-space()='Elements']")
    btn_click = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]")
    text_button = (By.XPATH, "//span[normalize-space()='Text Box']")
    full_name = (By.ID, "userName")
    email = (By.ID, "userEmail")
    address = (By.ID, "currentAddress")
    per_Add = (By.ID, "permanentAddress")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def element_page(self):
        element = self.wait.until(EC.presence_of_element_located(self.ele_btn_clk))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

        element2 = self.wait.until(EC.presence_of_element_located(self.btn_click))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element2)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element2)

    def text_box_button(self):
        element = self.wait.until(EC.presence_of_element_located(self.text_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

        heading = self.driver.find_element(By.XPATH, "//h1[text()='Text Box']")
        print(heading.text)
        time.sleep(3)

    def enter_full_name(self):
        self.driver.find_element(*self.full_name).send_keys("prem khedakar")

    def enter_email(self):
        self.driver.find_element(*self.email).send_keys("premkhedakar@gmail.com")

    def enter_address(self):
        self.driver.find_element(*self.address).send_keys("malai Pura")

    def enter_perm_add(self):
        self.driver.find_element(*self.per_Add).send_keys("malai Pura")

    def click_button_submit(self):
        button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", button)
