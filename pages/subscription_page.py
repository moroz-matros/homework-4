from pages.base_page import Page


class SubscriptionPage(Page):
    ACTIVE_TAB = '.tab-active'
    NO_ONE = 'h6'
    CONTAINER = '.search-main-block'

    SUBSCRIBED_TO = '#followedUsersTab'
    SUBSCRIBERS = '#followersTab'

    SUB_NAME = '.one-user-block__title'

    def get_active_tab_title(self):
        tab = self.wait_clickable_until_and_get_elem_by_css(self.ACTIVE_TAB)
        return tab.text

    def get_no_one_text(self):
        try:
            text = self.wait_visibility_until_and_get_elem_by_css(self.NO_ONE)
        except:
            text = self.wait_visibility_until_and_get_elem_by_css(self.NO_ONE)
        return text.text

    def redirect_to_subscribed_to(self):
        tab = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBED_TO)
        tab.click()

    def redirect_to_subscribers(self):
        tab = self.wait_clickable_until_and_get_elem_by_css(self.SUBSCRIBERS)
        tab.click()

    def get_sub_name(self):
        while not self.if_exists_css(self.SUB_NAME):
            continue
        text = self.get_element_by_css(self.SUB_NAME)
        return text.text
