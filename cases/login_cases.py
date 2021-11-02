import random
import string
from cases.base_cases import Test
from pages.login_page import LoginPage
from pages.main.navbar_page import NavbarPage
from pages.registration_page import RegistrationPage

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

    def test_login_ok(self):
        # Авторизация с корректным логином (при корректном пароле).

        self.page.open()
        self.page.fill_form(self.LOGIN, self.PASSWORD)
        self.page.click_login_button()

        navbar = NavbarPage(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(self.LOGIN, login_text)

    def test_login_wrong_login(self):
        # Ошибка при авторизации: с неверным логином

        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(rand_string, self.PASSWORD)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, error_text)

    def test_login_short_login(self):
        # Ошибка при авторизации: с коротким логином (<6 символов).

        self.page.open()
        self.page.fill_form(short_login, self.PASSWORD)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_login_with_punctuation_marks(self):
        # Ошибка при авторизации: с логином со знаками препинания (кроме точки)

        self.page.open()
        self.page.fill_form(comma_login, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_login(self):
        # Ошибка при авторизации: с пустым логином.

        self.page.open()
        self.page.fill_form(empty_string, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_wrong_password(self):
        # Ошибка при авторизации: с неверным паролем

        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(self.LOGIN, rand_string)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(INCORRECT_LOGIN_OR_PASSWORD, error_text)

    def test_login_empty_password(self):
        # Ошибка при авторизации: c пустым паролем.

        self.page.open()
        self.page.fill_form(good_login, empty_string)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_short_password(self):
        # Ошибка при авторизации: с коротким паролем (<7 символов).

        self.page.open()
        self.page.fill_form(good_login, short_password)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_redirect_to_registration(self):
        # Переадресация на страницу регистрации.

        self.page.open()
        self.page.click_redirect()

        registration_page = RegistrationPage(self.driver)
        text = registration_page.get_form_title()
        self.assertEqual(REGISTRATION_PAGE_TITLE, text)
