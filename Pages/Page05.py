import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page05:
    date_picker = (By.XPATH, "//span[normalize-space()='Date Picker']")
    select_date_input = (By.ID, "datePickerMonthYearInput")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_widget_btn(self):
        self.driver.get("https://demoqa.com/date-picker")
        time.sleep(2)

    def click_date_picker(self):
        element = self.wait.until(EC.presence_of_element_located(self.select_date_input))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def select_picker(self):
        pass  # ab zarurat nahi — click_date_picker hi open karta hai

    def click_select_month(self):
        sel = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
        sel.select_by_visible_text("June")

    def click_select_year(self):
        sel = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
        sel.select_by_visible_text("2026")

    def click_select_time(self):
        pass  # Select Date picker mein time nahi hota — sirf Date And Time picker mein

    def click_select_date(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@aria-label='Choose Saturday, June 13th, 2026']")
            )
        ).click()
        self.driver.save_screenshot("Screenshots/select_date_successfully.png")
        time.sleep(2)
