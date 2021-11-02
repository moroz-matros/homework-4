from cases.base_cases import Test
from pages.login_page import LoginPage
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

LOGIN_PAGE_TITLE = 'Вход'

LOGIN_ERROR_TEXT = 'Логин должен содержать минимум 5 символов латиницы, не содержать знаков препинания, кроме точки.'
LOGIN_EXISTING_ERROR_TEXT = 'Такой логин уже существует'

PASSWORD_ERROR_TEXT = 'Пароль должен содержать минимум 6 символов латиницы, цифр.'

NAME_ERROR_TEXT = 'Имя не должно быть пустым или содержать цифры, спецсимволы и знаки препинания.'


class RegistrationTest(Test):
    def setUp(self):
        super().setUp()
        self.page = RegistrationPage(self.driver)

    def test_registration_short_login(self):
        # Ошибка при регистрации: короткого логина (<6 символов).

        self.page.open()
        self.page.fill_form(short_login, good_password, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_login_with_punctuation_marks(self):
        # Ошибка при регистрации: логина со знаками препинания (кроме точки)

        self.page.open()
        self.page.fill_form(comma_login, good_password, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_empty_login(self):
        # Ошибка при регистрации: пустого логина

        self.page.open()
        self.page.fill_form(empty_string, good_password, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_login_error()

        self.assertEqual(LOGIN_ERROR_TEXT, error_text)

    def test_registration_existing_login(self):
        # Ошибка при регистрации: уже существующего логина

        self.page.open()
        self.page.fill_form(self.LOGIN, self.PASSWORD, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_existing_login_error()

        self.assertEqual(LOGIN_EXISTING_ERROR_TEXT, error_text)

    def test_registration_short_password(self):
        # Ошибка при регистрации: короткого пароля (<7 символов).

        self.page.open()
        self.page.fill_form(good_login, short_password, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_registration_empty_password(self):
        # Ошибка при регистрации: пустого пароля.

        self.page.open()
        self.page.fill_form(good_login, empty_string, good_name)
        self.page.click_registration_button()

        error_text = self.page.get_password_error()

        self.assertEqual(PASSWORD_ERROR_TEXT, error_text)

    def test_registration_number_in_name(self):
        # Ошибка при регистрации: имени с цифрами.

        self.page.open()
        self.page.fill_form(good_login, good_password, number_name)
        self.page.click_registration_button()

        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_empty_name(self):
        # Ошибка при регистрации: пустого имени.

        self.page.open()
        self.page.fill_form(good_login, good_password, empty_string)
        self.page.click_registration_button()

        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_name_with_punctuation_marks(self):
        # Ошибка при регистрации: имени со знаками препинания.

        self.page.open()
        self.page.fill_form(good_login, good_password, comma_name)
        self.page.click_registration_button()

        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_special_name(self):
        # Ошибка при регистрации: имени со специальными символами.

        self.page.open()
        self.page.fill_form(good_login, good_password, special_name)
        self.page.click_registration_button()

        error_text = self.page.get_name_error()

        self.assertEqual(NAME_ERROR_TEXT, error_text)

    def test_registration_redirect_to_login(self):
        # Переадресация на страницу авторизации.

        self.page.open()
        self.page.click_redirect()

        login_page = LoginPage(self.driver)
        text = login_page.get_form_title()
        self.assertEqual(LOGIN_PAGE_TITLE, text)


'''
    def test_registration_good(self):
        # Регистрация с корректным логином (при других корректных полях).
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))

        self.steps.register(rand_string + '.', rand_string, rand_string)

        navbar = NavbarSteps(self.driver)
        login_text = navbar.get_login()
        self.assertEqual(rand_string, login_text)
'''
