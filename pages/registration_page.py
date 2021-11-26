from pages.base_page import Page


class RegistrationPage(Page):
    BASE_URL = 'https://qdaqda.ru/signup'

    FORM_TITLE = '.form__title'

    LOGIN_INPUT = 'input[name="login"]'
    PASSWORD_INPUT = 'input[name="password"]'
    NAME_INPUT = 'input[name="name"]'
    REGISTRATION_BUTTON = '#postRegistration'
    REDIRECT = '.form__bottom-text_anchor'
    CONTAINER = '.container'

    LOGIN_ERROR = '#loginError'
    PASSWORD_ERROR = '#passwordError'
    NICKNAME_ERROR = '#nicknameError'

    def fill_form(self, login, password, name):
        login_input = self.wait_visibility_until_and_get_elem_by_css(self.LOGIN_INPUT)
        password_input = self.wait_visibility_until_and_get_elem_by_css(self.PASSWORD_INPUT)
        name_input = self.wait_visibility_until_and_get_elem_by_css(self.NAME_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)
        name_input.send_keys(name)

    def click_registration_button(self):
        button = self.wait_clickable_until_and_get_elem_by_css(self.REGISTRATION_BUTTON)
        button.click()

    def click_redirect(self):
        button = self.wait_clickable_until_and_get_elem_by_css(self.REDIRECT)
        button.click()

    def get_form_title(self):
        title = self.wait_visibility_until_and_get_elem_by_css(self.FORM_TITLE)
        return title.text

    def get_login_error(self):
        error = self.wait_visibility_until_and_get_elem_by_css(self.LOGIN_ERROR)
        return error.text

    def get_existing_login_error(self):
        error = self.wait_visibility_until_and_get_elem_by_css(self.NICKNAME_ERROR)
        return error.text

    def get_password_error(self):
        error = self.wait_visibility_until_and_get_elem_by_css(self.PASSWORD_ERROR)
        return error.text

    def get_name_error(self):
        error = self.wait_visibility_until_and_get_elem_by_css(self.NICKNAME_ERROR)
        return error.text


