from pages.base_page import Page


class EventsPage(Page):
    BASE_URL = 'https://qdaqda.ru/events'
    PATH = ''

    CARD_CLASS = '.events-block'
    CARD_TITLE = '.events-block__title'
    CARD_PIC = '.events-block__photo'
    TAB_INACTIVE_CLASS = '.button-category_inactive'
    TAB_ACTIVE_CLASS = '.button-category_active'
    NOTIFICATION_TITLE_CLASS = '.notification-empty__title'
    NEAR_TAB = '[data-category="Ближайшие"]'
    CONTAINER = '.events-table'

    RECOMMEND = '#jsRecommendButton'

    def get_first_card_title(self):
        card = self.wait_visibility_until_and_get_elem_by_css(self.CARD_TITLE)
        return card.text

    def get_first_card_pic(self):
        card = self.wait_clickable_until_and_get_elem_by_css(self.CARD_PIC)
        return card

    def redirect_to_first_card_by_pic(self):
        pic = self.wait_clickable_until_and_get_elem_by_css(self.CARD_PIC)
        pic.click()

    def redirect_to_first_card_by_card(self):
        card = self.wait_clickable_until_and_get_elem_by_css(self.CARD_CLASS)
        card.click()

    def redirect_to_first_inactive_category_tab(self):
        tab = self.wait_clickable_until_and_get_elem_by_css(self.TAB_INACTIVE_CLASS)
        tab.click()

    def get_first_inactive_tab_title(self):
        tab = self.wait_visibility_until_and_get_elem_by_css(self.TAB_INACTIVE_CLASS)
        return tab.text

    def get_active_tab_name(self):
        tab = self.wait_visibility_until_and_get_elem_by_css(self.TAB_ACTIVE_CLASS)
        return tab.text

    def get_notification_text(self):
        n = self.wait_visibility_until_and_get_elem_by_css(self.NOTIFICATION_TITLE_CLASS)
        return n.text

    def redirect_to_near_tab(self):
        tab = self.wait_clickable_until_and_get_elem_by_css(self.NEAR_TAB)
        tab.click()

    def get_notification_title(self):
        title = self.wait_visibility_until_and_get_elem_by_css(self.NOTIFICATION_TITLE_CLASS)
        return title.text

    def get_recommend_tab(self):
        tab = self.wait_visibility_until_and_get_elem_by_css(self.RECOMMEND)
        return tab
