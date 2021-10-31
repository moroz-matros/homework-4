import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    page = None
    steps = None

    def setUp(self):
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.LOGIN = os.getenv('LOGIN')
        self.PASSWORD = os.getenv('PASSWORD')
        self.NAME = os.getenv('NAME')

    def go_to_main(self):
        self.page.open(self.page.BASE_URL)

    def tearDown(self):
        self.driver.quit()
