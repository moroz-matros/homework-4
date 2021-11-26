from pages.base_page import Page


class EventPage(Page):
    BASE_URL = 'https://qdaqda.ru/event'
    PATH = ''

    TITLE = '.event-description__title'

    STAR = '#jsEventStar'
    STATUS_TEXT = '#jsGoingText'

    CATEGORY = '.button-category_inactive'

    INVITE_BUTTON = '#jsEventShare'
    FRIENDS_LIST = '#jsEventFollowers'

    SHARE_BUTTON = '#jsSocialShare'
    VK_BUTTON = '#vkshare0'
    COPY_BUTTON = '#copyButton'

    DESCRIPTION = '.event-description__body'

    def get_title(self):
        title = self.wait_visibility_until_and_get_elem_by_css(self.TITLE)
        return title.text

    def click_star(self):
        star = self.wait_clickable_until_and_get_elem_by_css(self.STAR)
        star.click()

    def click_share(self):
        button = self.wait_clickable_until_and_get_elem_by_css(self.SHARE_BUTTON)
        button.click()

    def get_vk_button(self):
        return self.wait_clickable_until_and_get_elem_by_css(self.VK_BUTTON)

    def get_copy_button(self):
        return self.wait_clickable_until_and_get_elem_by_css(self.COPY_BUTTON)

    def get_friends_list(self):
        return self.wait_visibility_until_and_get_elem_by_css(self.FRIENDS_LIST)

    def click_invite(self):
        button = self.wait_clickable_until_and_get_elem_by_css(self.INVITE_BUTTON)
        button.click()

    def get_status_text(self):
        status = self.wait_visibility_until_and_get_elem_by_css(self.STATUS_TEXT)
        return status.text

    def get_first_tag_text(self):
        tag = self.wait_visibility_until_and_get_elem_by_css(self.CATEGORY)
        return tag.text

    def redirect_first_tag_search(self):
        tag = self.wait_clickable_until_and_get_elem_by_css(self.CATEGORY)
        tag.click()

    def get_description(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.DESCRIPTION)
        return text.text
