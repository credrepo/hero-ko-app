import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page05:
    ELEMENTS_CARD = (
        By.XPATH,
        "//h5[normalize-space()='Elements']"
    )

    window_widget = (
        By.XPATH,
        "//body/div[@id='root']/div[contains(@class,'body-height')]/div[contains(@class,'container playgound-body')]/div[contains(@class,'row')]/div[contains(@class,'col-md-3 col-xl-2')]/div[@class='left-pannel']/div[@class='accordion']/div[1]/span[1]/div[1]/div[1]"
    )

    date_picker = (
        By.XPATH,
        "//span[normalize-space()='Date Picker']"
    )

    select_date = (
        By.XPATH,
        "//input[@id='datePickerMonthYearInput']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_widget_btn(self):
        elements_card = self.wait.until(
            EC.presence_of_element_located(self.ELEMENTS_CARD)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            elements_card
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].click();",
            elements_card
        )

        elements_card = self.wait.until(
            EC.presence_of_element_located(self.window_widget)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            elements_card
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].click();",
            elements_card
        )

    def click_date_picker(self):
        buttons_menu = self.wait.until(
            EC.presence_of_element_located(self.date_picker)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            buttons_menu
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].click();",
            buttons_menu
        )

    def select_picker(self):
        buttons_menu = self.wait.until(
            EC.presence_of_element_located(self.select_date)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            buttons_menu
        )
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].click();",
            buttons_menu
        )

    def click_select_month(self):
        sel = Select(
            self.driver.find_element(
                By.XPATH,
                "//select[@class='react-datepicker__month-select']"
            )
        )
        sel.select_by_visible_text("June")

    def click_select_year(self):
        sel = Select(
            self.driver.find_element(
                By.XPATH,
                "//select[@class='react-datepicker__year-select']"
            )
        )
        sel.select_by_visible_text("2026")

    def click_select_date(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@aria-label='Choose Saturday, June 13th, 2026']"
                )
            )
        ).click()

        self.driver.save_screenshot(
            r"Screenshots\select_date_and_time_successfully.png"
        )

        time.sleep(2)

    def click_select_time(self):
        self.driver.save_screenshot("before_time_selection.png")

        times = self.driver.find_elements(
            By.XPATH,
            "//li[contains(@class,'react-datepicker__time-list-item')]"
        )

        print("\n===== AVAILABLE TIMES =====")
        for t in times:
            print(t.text)

        time_locator = (
            By.XPATH,
            "//li[contains(@class,'react-datepicker__time-list-item') and contains(.,'12:00')]"
        )

        time_option = self.wait.until(
            EC.element_to_be_clickable(time_locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            time_option
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            time_option
        )

        self.driver.save_screenshot(
            r"Screenshots\select_date_and_time_successfully.png"
        )

        time.sleep(2)
