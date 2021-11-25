from pages.base_page import Page


class ProfilePage(Page):
    BASE_URL = 'https://qdaqda.ru/profile'
    PATH = ''
    FILE_INPUT = '#imageFile'
    CONTAINER = '.container'

    CHANGE_AVATAR_BUTTON = '.change-avatar-button'
    AVATAR_IMAGE = '.my-profile-header__avatar-block'

    def change_avatar(self):
        tag = self.wait_until_and_get_elem_by_css(self.CHANGE_AVATAR_BUTTON)
        tag.click()

    def send_file(self, open, path):
        open()

        avatar_input = self.locate_hidden_el(self.FILE_INPUT)
        avatar_input.send_keys(path)

        # # closing file select dialog
        # # this probably won't work on macOS
        # self.close_browser_dialogue()

    def get_avatar_url(self):
        return self.wait_until_and_get_elem_by_css(self.AVATAR_IMAGE).get_attribute('style').split("\"", 2)[1]





