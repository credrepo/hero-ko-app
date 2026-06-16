import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page05:
    window_widget = (By.XPATH, "//body/div[@id='root']/div[contains(@class,'body-height')]/div[contains(@class,'container playgound-body')]/div[contains(@class,'row')]/div[contains(@class,'col-md-3 col-xl-2')]/div[@class='left-pannel']/div[@class='accordion']/div[1]/span[1]/div[1]/div[1]")
    date_picker = (By.XPATH, "//span[normalize-space()='Date Picker']")
    select_date_input = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    date_and_time_input = (By.XPATH, "//input[@id='dateAndTimePickerInput']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_widget_btn(self):
        element = self.wait.until(EC.presence_of_element_located(self.window_widget))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def click_date_picker(self):
        element = self.wait.until(EC.presence_of_element_located(self.date_picker))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def select_picker(self):
        element = self.wait.until(EC.presence_of_element_located(self.select_date_input))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def click_select_month(self):
        sel = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
        sel.select_by_visible_text("June")

    def click_select_year(self):
        sel = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
        sel.select_by_visible_text("2026")

    def click_select_time(self):
        time_locator = (By.XPATH, "//li[contains(@class,'react-datepicker__time-list-item') and normalize-space()='12:00']")
        time_option = self.wait.until(EC.presence_of_element_located(time_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", time_option)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", time_option)

    def click_select_date(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@aria-label='Choose Saturday, June 13th, 2026']")
            )
        ).click()
        self.driver.save_screenshot("Screenshots/select_date_and_time_successfully.png")
        time.sleep(2)
