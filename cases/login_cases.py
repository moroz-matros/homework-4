import random
import string
from cases.base_cases import Test
from pages.login_page import LoginPage
from pages.navbar_page import NavbarPage
from pages.registration_page import RegistrationPage


letters = string.ascii_lowercase

short_login = 'bad'
comma_login = 'bad,'

empty_string = ''
long_string = 'q' * 257

short_password = 'bad'
comma_password = ',qqqqqq'

number_name = 'name11'
comma_name = ',name'
special_name = '<name'

REGISTRATION_PAGE_TITLE = 'Регистрация'

INCORRECT_LOGIN_OR_PASSWORD = 'Неправильный логин или пароль'

LOGIN_ERROR_TEXT = 'Логин должен содержать минимум 5 символов латиницы, не содержать знаков препинания, кроме точки.'
LOGIN_EXISTING_ERROR_TEXT = 'Такой логин уже существует'
LOGIN_LONG_ERROR_TEXT = 'Превышена максимальная длина логина'

PASSWORD_ERROR_TEXT = 'Пароль должен содержать минимум 6 символов латиницы, цифр.'
PASSWORD_LONG_ERROR_TEXT = 'Превышена максимальная длина пароля'

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
        name_text = navbar.get_name()
        self.assertEqual(self.NAME, name_text)

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

        good_password = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(comma_login, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_login_empty_login(self):
        # Ошибка при авторизации: с пустым логином.

        good_password = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(empty_string, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    ''' <BUG>
    def test_login_long_login(self):
        # Ошибка при авторизации: с длинным логином (>256 символов). 

        self.page.open()
        self.page.fill_form(long_string, good_password)
        self.page.click_login_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_LONG_ERROR_TEXT, error_text)
    '''

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

        good_login = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(good_login, empty_string)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_login_short_password(self):
        # Ошибка при авторизации: с коротким паролем (<7 символов).

        good_login = ''.join(random.choice(letters) for i in range(10))

        self.page.open()
        self.page.fill_form(good_login, short_password)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    ''' <BUG>
    def test_login_long_password(self):
        # Ошибка при авторизации: с длинным паролем (>256 символов). <BUG>

        self.page.open()
        self.page.fill_form(good_login, long_string)
        self.page.click_login_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_LONG_ERROR_TEXT, error_text)
    '''

    def test_login_redirect_to_registration(self):
        # Переадресация на страницу регистрации.

        self.page.open()
        self.page.click_redirect()

        registration_page = RegistrationPage(self.driver)
        text = registration_page.get_form_title()
        self.assertEqual(REGISTRATION_PAGE_TITLE, text)
