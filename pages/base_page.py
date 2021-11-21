import urllib.parse


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Page(object):
    BASE_URL = 'https://qdaqda.ru/'
    PATH = ''
    WAIT_TIME = 1.5

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.open(self.BASE_URL)

    def wait_until(self, cond_f, wait: float = None):
        if wait is None:
            wait = self.WAIT_TIME
        waiter = WebDriverWait(self.driver, wait)
        return waiter.until(cond_f)

    def wait_until_and_get_elem_by_xpath(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 15, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def wait_until_and_get_elem_by_css(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elem)))

    def wait_until_and_get_elem_by_id(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.ID, elem)))

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 30, 0.1).until(EC.url_to_be(url))

    def wait_for_page(self, container_css):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, container_css)))

    def locate_hidden_el(self, css_sel, wait: float = 3.0) -> WebElement:
        return self.wait_until(EC.presence_of_element_located((By.CSS_SELECTOR, css_sel)), wait)

    def open(self, url=None):
        if (url == None):
            url = self.BASE_URL
        url = urllib.parse.urljoin(url, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()
