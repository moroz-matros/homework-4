from pages.base_page import Page


class ActivityPage(Page):
    BASE_URL = 'https://qdaqda.ru/activity'
    PATH = ''

    CONTAINER = '.activity'
    ACTIVITY_BLOCK = '.activity-block'
    FRIEND = ':first-of-type.event-title_anchor'
    EVENT = ':last-of-type.event-title_anchor'

    def get_activity_block(self):
        try:
            block = self.wait_presence_until_and_get_elem_by_css(self.ACTIVITY_BLOCK)
        except:
            block = self.wait_presence_until_and_get_elem_by_css(self.ACTIVITY_BLOCK)
        return block

    def click_friend(self):
        name = self.wait_visibility_until_and_get_elem_by_css(self.FRIEND)
        name.click()

    def click_event(self):
        name = self.wait_visibility_until_and_get_elem_by_css(self.EVENT)
        name.click()
