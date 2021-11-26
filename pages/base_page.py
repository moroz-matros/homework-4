import urllib.parse

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Page(object):
    BASE_URL = 'https://qdaqda.ru/'

    WAIT_TIME = 1.5
    TIME = 10

    def __init__(self, driver):
        self.driver = driver

    def wait_visibility_until_and_get_elem_by_css(self, elem) -> WebElement:
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elem)))
        return self.driver.find_element(By.CSS_SELECTOR, elem)

    def wait_clickable_until_and_get_elem_by_css(self, elem) -> WebElement:
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, elem)))
        return self.driver.find_element(By.CSS_SELECTOR, elem)

    def get_element_by_css(self, elem):
        return self.driver.find_element(By.CSS_SELECTOR, elem)

    def wait_presence_until_and_get_elem_by_css(self, elem) -> WebElement:
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, elem)))
        return self.driver.find_element(By.CSS_SELECTOR, elem)

    def wait_until_and_get_elem_by_name(self, elem) -> WebElement:
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.visibility_of_element_located((By.NAME, elem)))
        return self.driver.find_element(By.NAME, elem)

    def wait_presence_until_and_get_elem_by_name(self, elem) -> WebElement:
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.presence_of_element_located((By.NAME, elem)))
        return self.driver.find_element(By.NAME, elem)

    def wait_for_page(self, container_css):
        WebDriverWait(self.driver, self.TIME, 0.1).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, container_css)))
        return self.driver.find_element(By.CSS_SELECTOR, container_css)

    def open(self, url=None):
        if (url == None):
            url = self.BASE_URL
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()





