from selenium import webdriver
from selenium.webdriver.common.by import By


class DriveSetter:
    driver = webdriver.Chrome()

    def access_page(self, url):
        self.driver.get(url)

    def close_driver(self):
        self.driver.close()

    def find_address_text(self, name: str):
        return self.driver.find_element(by=By.CLASS_NAME, value=name).text
