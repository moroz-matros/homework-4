import urllib.parse

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page(object):
    BASE_URL = 'https://qdaqda.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.open(self.BASE_URL)

    def wait_until_and_get_elem_by_xpath(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 15, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def wait_until_and_get_elem_by_css(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elem)))

    def wait_until_and_get_elem_by_id(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.ID, elem)))

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 30, 0.1).until(EC.url_to_be(url))

    def open(self, url=None):
        if (url == None):
            url = self.BASE_URL
        url = urllib.parse.urljoin(url, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()