import os
import string
import unittest
import random

from selenium.webdriver import DesiredCapabilities, Remote
from cases.base_cases import Test
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from steps.main.navbar_steps import NavbarSteps
from steps.registration_steps import RegistrationSteps

good_login = 'sunny'
short_login = 'bad'
comma_login = 'bad,'

empty_string = ''

good_password = 'password'
short_password = 'bad'
comma_password = ',qqqqqq'

good_name = 'name'
number_name = 'name11'
comma_name = ',name'
special_name = '<name'

LOGIN_PAGE_TITLE = 'Вход'

LOGIN_ERROR_TEXT = 'Логин должен содержать минимум 5 символов латиницы, не содержать знаков препинания, кроме точки.'
LOGIN_EXISTING_ERROR_TEXT = 'Такой логин уже существует'

PASSWORD_ERROR_TEXT = 'Пароль должен содержать минимум 6 символов латиницы, цифр.'

NAME_ERROR_TEXT = 'Имя не должно быть пустым или содержать цифры, спецсимволы и знаки препинания.'


class RegistrationTest(Test):
    def setUp(self):
        super().setUp()
        self.page = RegistrationPage(self.driver)
        self.steps = RegistrationSteps(self.driver)

    def test_registration_short_login(self):
        self.steps.register(short_login, good_password, good_name)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_login_with_punctuation_marks(self):
        self.steps.register(comma_login, good_password, good_name)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_empty_login(self):
        self.steps.register(empty_string, good_password, good_name)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_existing_login(self):
        self.steps.register(self.LOGIN, self.PASSWORD, good_name)
        error_text = self.page.get_existing_login_error()

        self.assertEqual(LOGIN_EXISTING_ERROR_TEXT, error_text)

    def test_registration_short_password(self):
        self.steps.register(good_login, short_password, good_name)
        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_registration_empty_password(self):
        self.steps.register(good_login, empty_string, good_name)
        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_registration_number_in_name(self):
        self.steps.register(good_login, good_password, number_name)
        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_empty_name(self):
        self.steps.register(good_login, good_password, empty_string)
        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_name_with_punctuation_marks(self):
        self.steps.register(good_login, good_password, comma_name)
        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_special_name(self):
        self.steps.register(good_login, good_password, special_name)
        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_redirect_to_login(self):
        self.steps.redirect_to_login()

        login_page = LoginPage(self.driver)
        text = login_page.get_form_title()
        self.assertEqual(LOGIN_PAGE_TITLE, text)


'''
    def test_registration_good(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.steps.register(rand_string + '.', rand_string, rand_string)

        navbar = NavbarSteps(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(rand_string, login_text)
'''
