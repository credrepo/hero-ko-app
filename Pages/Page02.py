import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page02:
    download_btn = (By.ID, "downloadButton")
    upload_btn = (By.ID, "uploadFile")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def element_page(self):
        pass  # ab zarurat nahi

    def upload_and_download(self):
        self.driver.get("https://demoqa.com/upload-download")
        time.sleep(2)

    def download(self):
        element = self.wait.until(EC.presence_of_element_located(self.download_btn))
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        self.driver.find_element(*self.upload_btn).send_keys(r"C:\Users\Shubham\Desktop\mantra.txt")
        self.driver.save_screenshot("Screenshots/download_and_upload_successfully.png")
        time.sleep(2)
