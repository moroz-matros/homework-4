import random
import string
import time
from selenium.webdriver.support.wait import WebDriverWait

from cases.base_cases import Test
from pages.profile_page import ProfilePage

letters = string.ascii_lowercase


class ProfileChangeTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.login()
        self.page.open()

    def tearDown(self):
        self.page.open()
        self.page.redirect_to_about()
        self.page.fill_name(self.NAME)
        self.page.click_save_changes()
        super().tearDown()

    def test_profile_changes_ok(self):
        new_name = ''.join(random.choice(letters) for i in range(10))
        n = random.randint(10, 27)
        new_about = ''.join(random.choice(letters) for i in range(10))
        new_date = '2000-01-' + str(n)
        new_city = ''.join(random.choice(letters) for i in range(10))
        new_email = ''.join(random.choice(letters) for i in range(10)) + '@lala.ru'

        # self.page.redirect_to_about()
        self.page.open("https://qdaqda.ru/profile?tab=aboutTab")
        self.page.wait_for_page(self.page.CONTAINER_BOTTOM)

        # time.sleep(2)

        while True:
            self.page.fill_name(new_name)
            self.page.fill_about(new_about)
            self.page.fill_birthday(new_date)
            self.page.fill_city(new_city)
            self.page.fill_email(new_email)

            if (new_name == self.page.get_name() and
                    new_about == self.page.get_about() and
                    new_date == self.page.get_birthday() and
                    new_city == self.page.get_city() and
                    new_email == self.page.get_email()):
                break

        # time.sleep(100)

        self.page.click_save_changes()

        self.page.open("https://qdaqda.ru/profile?tab=aboutTab")
        # self.page.redirect_to_about()

        # time.sleep(2)
        while True:
            name = self.page.get_name()
            about = self.page.get_about()
            date = self.page.get_birthday()
            city = self.page.get_city()
            email = self.page.get_email()

            if (name == self.page.get_name() and
                    about == self.page.get_about() and
                    date == self.page.get_birthday() and
                    city == self.page.get_city() and
                    email == self.page.get_email()):
                break

        print(name)
        self.assertEqual(new_name, name)
        self.assertEqual(new_about, about)
        self.assertEqual(new_date, date)
        self.assertEqual(new_city, city)
        self.assertEqual(new_email, email)
