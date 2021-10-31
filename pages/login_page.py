from pages.base_page import Page


class LoginPage(Page):
    BASE_URL = 'https://qdaqda.ru/login'
    PATH = ''

    FORM_TITLE = '.form__title'

    LOGIN_INPUT = 'input[name="login"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = '#postLogin'
    REDIRECT = '.form__bottom-text_anchor'

    LOGIN_ERROR = '#loginError'
    PASSWORD_ERROR = '#passwordError'

    def fill_form(self, login, password):
        login_input = self.wait_until_and_get_elem_by_css(self.LOGIN_INPUT)
        password_input = self.wait_until_and_get_elem_by_css(self.PASSWORD_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)

    def click_login_button(self):
        button = self.wait_until_and_get_elem_by_css(self.LOGIN_BUTTON)
        button.click()

    def get_form_title(self):
        title = self.wait_until_and_get_elem_by_css(self.FORM_TITLE)
        return title.text

    def get_login_error(self):
        error = self.wait_until_and_get_elem_by_css(self.LOGIN_ERROR)
        return error.text

    def get_password_error(self):
        error = self.wait_until_and_get_elem_by_css(self.PASSWORD_ERROR)
        return error.text

    def click_redirect(self):
        button = self.wait_until_and_get_elem_by_css(self.REDIRECT)
        button.click()
