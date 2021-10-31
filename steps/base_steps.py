from selenium.webdriver import Remote


class BaseSteps(object):
    def __init__(self, driver: Remote):
        self.driver = driver