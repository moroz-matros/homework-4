import os
import random
import string
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from cases.base_cases import Test
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from steps.login_steps import LoginSteps
from steps.main.navbar_steps import NavbarSteps

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

REGISTRATION_PAGE_TITLE = 'Регистрация'

INCORRECT_LOGIN_OR_PASSWORD = 'Неправильный логин или пароль'

LOGIN_ERROR_TEXT = 'Логин должен содержать минимум 5 символов латиницы, не содержать знаков препинания, кроме точки.'
LOGIN_EXISTING_ERROR_TEXT = 'Такой логин уже существует'

PASSWORD_ERROR_TEXT = 'Пароль должен содержать минимум 6 символов латиницы, цифр.'

NAME_ERROR_TEXT = 'Имя не должно быть пустым или содержать цифры, спецсимволы и знаки препинания.'


class LoginTest(Test):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)
        self.steps = LoginSteps(self.driver)

    def test_login_ok(self):
        self.steps.login(self.LOGIN, self.PASSWORD)

        navbar = NavbarSteps(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(self.LOGIN, login_text)

    def test_login_wrong_login(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.steps.login(rand_string, self.PASSWORD)
        error_text = self.page.get_password_error()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, error_text)

    def test_login_wrong_password(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.steps.login(self.LOGIN, rand_string)
        error_text = self.page.get_password_error()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, error_text)

    def test_login_short_login(self):
        self.steps.login(short_login, self.PASSWORD)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_login_with_punctuation_marks(self):
        self.steps.login(comma_login, good_password)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_login(self):
        self.steps.login(empty_string, good_password)
        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_password(self):
        self.steps.login(good_login, empty_string)
        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_short_password(self):
        self.steps.login(good_login, short_password)
        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_redirect_to_registration(self):
        self.steps.redirect_to_registration()

        registration_page = RegistrationPage(self.driver)
        text = registration_page.get_form_title()
        self.assertEqual(REGISTRATION_PAGE_TITLE, text)


