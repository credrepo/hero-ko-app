import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page02:
    ele_btn_clk = (By.XPATH, "//h5[normalize-space()='Elements']")
    btn_click = (By.XPATH, "//body/div[@id='root']/div[contains(@class,'body-height')]/div[contains(@class,'container playgound-body')]/div[contains(@class,'row')]/div[contains(@class,'col-md-3 col-xl-2')]/div[@class='left-pannel']/div[@class='accordion']/div[1]/span[1]/div[1]/div[1]")
    ele_btn_clk1 = (By.ID, "item-7")
    download_btn = (By.XPATH, "//a[@id='downloadButton']")

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

    def upload_and_download(self):
        element = self.wait.until(EC.presence_of_element_located(self.ele_btn_clk1))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

    def download(self):
        element = self.wait.until(EC.presence_of_element_located(self.download_btn))
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        self.driver.find_element(By.ID, "uploadFile").send_keys(r"C:\Users\Shubham\Desktop\mantra.txt")
        self.driver.save_screenshot("Screenshots/download_and_upload_successfully.png")
        time.sleep(2)
