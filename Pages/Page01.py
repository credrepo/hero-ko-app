import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page01:
    ele_btn_clk = (By.XPATH,"//h5[normalize-space()='Elements']")
    btn_click = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]")
    text_button = (By.XPATH, "//span[normalize-space()='Text Box']")
    full_name = (By.ID,"userName")
    email = (By.ID, "userEmail")
    address = (By.ID, "currentAddress")
    per_Add = (By.ID, "permanentAddress")




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_page_title(self):
        assert self.driver.title == "demosite", f"Actual title: {self.driver.title}"
        print("Title matched")

    def element_page(self):
        self.wait.until(EC.element_to_be_clickable(self.ele_btn_clk)).click()
        self.wait.until(EC.element_to_be_clickable(self.btn_click)).click()


    def text_box_button(self):
        self.wait.until(EC.element_to_be_clickable(self.text_button)).click()
        element = self.driver.find_element(By.XPATH, "//h1[text()='Text Box']")
        element.is_displayed()
        print(element.text)
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
        self.driver.find_element(By.ID, "submit").click()
