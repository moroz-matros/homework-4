import random
import string
import time

from cases.base_cases import Test
from pages.profile_page import ProfilePage

letters = string.ascii_lowercase
PASSWORD_CHANGE_SUCCESS = 'Пароль успешно изменен.'


class ProfilePasswordChangeTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.login()
        self.page.open()

    def tearDown(self):
        self.page.fill_old_password(self.new_password)
        self.page.fill_new_password(self.PASSWORD)
        self.page.click_save_changes()
        super().tearDown()

    def test_profile_settings_change_ok(self):
        # Сохраняет при вводе корректных старого и нового паролей (новый пароль >=6 символов).

        self.new_password = ''.join(random.choice(letters) for i in range(10))

        # self.page.redirect_to_settings()
        self.page.open("https://qdaqda.ru/profile?tab=settingsTab")
        self.page.wait_for_page(self.page.CONTAINER_BOTTOM)

        self.page.fill_old_password(self.PASSWORD)
        self.page.fill_new_password(self.new_password)

        self.page.click_save_changes()

        success = self.page.get_password_success()

        self.assertEqual(PASSWORD_CHANGE_SUCCESS, success)
