import os
import pathlib

from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import Page
import pyautogui


class ProfilePage(Page):
    BASE_URL = 'https://qdaqda.ru/profile'

    TITLE_CLASS = '.smbs-event__title'
    SUBSCRIBER = ':first-of-type.my-profile-header__followers-block'
    SUBSCRIBED_TO = ':last-of-type.my-profile-header__followers-block'
    USER_NAME = '.profile-header__title'

    CONTAINER = '.page-photo_profile'
    SUBSCRIBE_BUTTON = '#subscribeUserButton'

    ABOUT_TAB = '#aboutTab'
    SETTINGS_TAB = '#settingsTab'

    UPLOAD_AVATAR_BUTTON = '#jsUploadAvatar'
    NEW_AVATAR = '#imageFile'
    AVATAR = '#profileAvatar'
    SUBMIT_AVATAR = '#jsSubmitAvatar'
    AVATAR_ERROR = '#jsErrorAvatar'

    EVENT_CUBE = '.smbs-event-cube'
    ARROW_DOWN = '.smbs-event__arrow-down'
    ARROW_UP = '.smbs-event__arrow-up'
    TOP_SIDE = '.smbs-event-cube_show_top'
    EVENT_DESCRIPTION = '.smbs-event__text'
    CONTAINER_DESCRIPTION = '.smbs-event_top_side'
    EVENT_TITLE = '.smbs-event__title'
    SHARE_BUTTON = '.smbs-event__share-button'
    VK_BUTTON = '#shareButtonsBlock'
    COPY_BUTTON = '#copyButton'

    NAME = 'name'
    ABOUT = 'about'
    DATE = 'birthday'
    CITY = 'city'
    EMAIL = 'email'
    SAVE_BUTTON = '#postProfile'
    CONTAINER_BOTTOM = '#changing-content'
    PROFILE_NAME = '.my-profile-header__title'

    NAME_ERROR = '#nicknameError'
    ABOUT_ERROR = '#aboutError'
    DATE_ERROR = '#birthdayError'
    CITY_ERROR = '#cityError'
    EMAIL_ERROR = '#emailError'

    OLD_PASSWORD = 'oldPassword'
    NEW_PASSWORD = 'newPassword'
    PASSWORD_ERROR = '#jsPasswordError'
    PASSWORD_SUCCESS = '#jsPasswordSuccess'

    SHARE = '.share-modal'

    def get_first_event_title(self):
        title = self.wait_visibility_until_and_get_elem_by_css(self.TITLE_CLASS)
        return title.text

    def get_user_name(self):
        name = self.wait_visibility_until_and_get_elem_by_css(self.USER_NAME)
        return name.text

    def redirect_to_subscribers(self):
        try:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBER)
            button.click()
        except StaleElementReferenceException:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBER)
            button.click()

    def redirect_to_subscribed_to(self):
        try:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBED_TO)
            button.click()
        except StaleElementReferenceException:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBED_TO)
            button.click()

    def upload_avatar(self, text):
        dir = str(pathlib.Path(__file__).parent.parent)
        try:
            button = self.wait_presence_until_and_get_elem_by_css(self.NEW_AVATAR)
            button.send_keys(dir + text)
        except:
            button = self.wait_presence_until_and_get_elem_by_css(self.NEW_AVATAR)
            button.send_keys(dir + text)

    def get_avatar_pic_style(self):
        avatar = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR)
        return avatar.get_attribute('style')

    def get_new_avatar_pic_style(self, old):
        while not self.if_exists_css(self.AVATAR):
            continue
        try:
            avatar = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR)
            style = avatar.get_attribute('style')
        except:
            avatar = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR)
            style = avatar.get_attribute('style')
        while style == old:
            while not self.if_exists_css(self.AVATAR):
                continue
            try:
                avatar = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR)
                style = avatar.get_attribute('style')
            except:
                avatar = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR)
                style = avatar.get_attribute('style')
        return style

    def get_submit_avatar_button(self):
        button = self.wait_visibility_until_and_get_elem_by_css(self.SUBMIT_AVATAR)
        return button

    def is_exists_avatar_button(self):
        return self.if_exists_css(self.SUBMIT_AVATAR)


    def get_avatar_error(self):
        while not self.if_exists_css(self.AVATAR_ERROR):
            continue
        # TODO поставить на соответствие текста
        text = self.wait_visibility_until_and_get_elem_by_css(self.AVATAR_ERROR)
        return text.text

    def click_arrow_down(self):
        while not self.if_exists_css(self.ARROW_DOWN):
            continue
        try:
            button = self.wait_clickable_until_and_get_elem_by_css(self.ARROW_DOWN)
            button.click()
        except:
            button = self.wait_clickable_until_and_get_elem_by_css(self.ARROW_DOWN)
            button.click()

    def click_arrow_up(self):
        try:
            button = self.wait_clickable_until_and_get_elem_by_css(self.ARROW_UP)
            button.click()
        except:
            button = self.wait_clickable_until_and_get_elem_by_css(self.ARROW_UP)
            button.click()

    def get_event_description(self):
        try:
            text = self.wait_visibility_until_and_get_elem_by_css(self.EVENT_DESCRIPTION)
            return text.text
        except:
            text = self.wait_visibility_until_and_get_elem_by_css(self.EVENT_DESCRIPTION)
            return text.text

    def get_event_title(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.EVENT_TITLE)
        return text.text

    def click_share_button(self):
        while not self.if_exists_css(self.SHARE_BUTTON):
            continue
        try:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SHARE_BUTTON)
            button.click()
        except:
            button = self.wait_clickable_until_and_get_elem_by_css(self.SHARE_BUTTON)
            button.click()

    def get_vk_button(self):
        while not self.if_exists_css(self.VK_BUTTON):
            continue
        try:
            button = self.wait_visibility_until_and_get_elem_by_css(self.VK_BUTTON)
            return button
        except:
            button = self.wait_visibility_until_and_get_elem_by_css(self.VK_BUTTON)
            return button

    def get_copy_button(self):
        while not self.if_exists_css(self.VK_BUTTON):
            continue
        try:
            button = self.wait_visibility_until_and_get_elem_by_css(self.VK_BUTTON)
            return button
        except:
            button = self.wait_visibility_until_and_get_elem_by_css(self.VK_BUTTON)
            return button

    def fill_name(self, text):
        try:
            field = self.wait_presence_until_and_get_elem_by_name(self.NAME)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_presence_until_and_get_elem_by_name(self.NAME)
            field.clear()
            field.send_keys(text)

    def fill_about(self, text):
        try:
            field = self.wait_presence_until_and_get_elem_by_name(self.ABOUT)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_presence_until_and_get_elem_by_name(self.ABOUT)
            field.clear()
            field.send_keys(text)

    def fill_city(self, text):
        try:
            field = self.wait_presence_until_and_get_elem_by_name(self.CITY)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_presence_until_and_get_elem_by_name(self.CITY)
            field.clear()
            field.send_keys(text)

    def fill_birthday(self, text):
        try:
            field = self.wait_presence_until_and_get_elem_by_name(self.DATE)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_presence_until_and_get_elem_by_name(self.DATE)
            field.clear()
            field.send_keys(text)

    def fill_email(self, text):
        try:
            field = self.wait_presence_until_and_get_elem_by_name(self.EMAIL)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_presence_until_and_get_elem_by_name(self.EMAIL)
            field.clear()
            field.send_keys(text)

    def click_save_changes(self):
        try:
            button = self.wait_visibility_until_and_get_elem_by_css(self.SAVE_BUTTON)
            button.click()
        except:
            button = self.wait_visibility_until_and_get_elem_by_css(self.SAVE_BUTTON)
            button.click()

    def redirect_to_about(self):
        try:
            tab = self.wait_visibility_until_and_get_elem_by_css(self.ABOUT_TAB)
            tab.click()
        except:
            tab = self.wait_visibility_until_and_get_elem_by_css(self.ABOUT_TAB)
            tab.click()

    def get_name(self):
        try:
            field = self.wait_until_and_get_elem_by_name(self.NAME)
            return field.get_attribute('value')
        except:
            field = self.wait_until_and_get_elem_by_name(self.NAME)
            return field.get_attribute('value')

    def get_about(self):
        try:
            field = self.wait_until_and_get_elem_by_name(self.ABOUT)
            return field.get_attribute('value')
        except:
            field = self.wait_until_and_get_elem_by_name(self.ABOUT)
            return field.get_attribute('value')

    def get_city(self):
        try:
            field = self.wait_until_and_get_elem_by_name(self.CITY)
            return field.get_attribute('value')
        except:
            field = self.wait_until_and_get_elem_by_name(self.CITY)
            return field.get_attribute('value')

    def get_birthday(self):
        try:
            field = self.wait_until_and_get_elem_by_name(self.DATE)
            return field.get_attribute('value')
        except:
            field = self.wait_until_and_get_elem_by_name(self.DATE)
            return field.get_attribute('value')

    def get_email(self):
        try:
            field = self.wait_until_and_get_elem_by_name(self.EMAIL)
            return field.get_attribute('value')
        except:
            field = self.wait_until_and_get_elem_by_name(self.EMAIL)
            return field.get_attribute('value')

    def get_name_error_text(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.NAME_ERROR).text
        while text == '':
            try:
                text = self.wait_visibility_until_and_get_elem_by_css(self.NAME_ERROR).text
            except:
                text = self.wait_visibility_until_and_get_elem_by_css(self.NAME_ERROR).text
        return text

    def get_about_error_text(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.ABOUT_ERROR)
        return text.text

    def get_city_error_text(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.CITY_ERROR)
        return text.text

    def get_birthday_error_text(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.DATE_ERROR)
        return text.text

    def get_email_error_text(self):
        text = self.wait_presence_until_and_get_elem_by_css(self.EMAIL_ERROR)
        return text.text

    def redirect_to_settings(self):
        settings = self.wait_presence_until_and_get_elem_by_css(self.SETTINGS_TAB)
        settings.click()

    def fill_old_password(self, text):
        try:
            field = self.wait_until_and_get_elem_by_name(self.OLD_PASSWORD)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_until_and_get_elem_by_name(self.OLD_PASSWORD)
            field.clear()
            field.send_keys(text)

    def fill_new_password(self, text):
        try:
            field = self.wait_until_and_get_elem_by_name(self.NEW_PASSWORD)
            field.clear()
            field.send_keys(text)
        except:
            field = self.wait_until_and_get_elem_by_name(self.NEW_PASSWORD)
            field.clear()
            field.send_keys(text)

    def click_save_new_password(self):
        button = self.wait_visibility_until_and_get_elem_by_css(self.SAVE_BUTTON)
        button.click()

    def get_password_success(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.PASSWORD_SUCCESS)
        return text.text

    def get_password_error(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.PASSWORD_ERROR)
        return text.text

    def get_profile_name(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.PROFILE_NAME)
        return text.text

    def get_changed_profile_name(self):
        text = self.wait_presence_until_and_get_elem_by_css(self.PROFILE_NAME)
        while not text.is_enabled():
            continue
        return text.text

    def get_event_cube(self):
        cube = self.wait_presence_until_and_get_elem_by_css(self.EVENT_CUBE)
        return cube

    def is_exists_event_top(self):
        return self.if_exists_css(self.TOP_SIDE)

    def is_displayed_event_top(self):
        try:
            event_top = self.wait_visibility_until_and_get_elem_by_css(self.TOP_SIDE)
            return event_top.is_displayed()
        except:
            event_top = self.wait_visibility_until_and_get_elem_by_css(self.TOP_SIDE)
            return event_top.is_displayed()


    def is_exists_share_window(self):
        return self.if_exists_css(self.SHARE)