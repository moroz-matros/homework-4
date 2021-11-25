from pages.base_page import Page


class ChatPage(Page):
    BASE_URL = 'https://qdaqda.ru/chat'
    PATH = ''

    CONTAINER = '.chat'
    CURRENT_CHAT_USER_NAME = '#jsNameCompanion'
    LAST_MESSAGE = ':last-of-type.chat__message_my'
    SEND_BUTTON = '#jsSendMessageButton'
    INPUT = '.send-message-textarea'
    CARD_LEFT = ':first-of-type.message_read'

    def get_current_chat_user_name(self):
        name = self.wait_until_and_get_elem_by_css(self.CURRENT_CHAT_USER_NAME)
        return name.text

    def get_last_message_text(self):
        message = self.wait_until_and_get_elem_by_css(self.LAST_MESSAGE)
        return message.text

    def click_send_button(self):
        button = self.wait_until_and_get_elem_by_css(self.SEND_BUTTON)
        button.click()

    def write_message(self, s):
        line = self.wait_until_and_get_elem_by_css(self.INPUT)
        line.send_keys(s)

    def get_left_card_color(self):
        card = self.wait_until_and_get_elem_by_css(self.CARD_LEFT)
        return card.get_attribute('style')

    def click_left_card(self):
        card = self.wait_until_and_get_elem_by_css(self.INPUT)
        card.click()

    def click_link(self, ref):
        link = self.driver.find_element_by_link_text(ref)
        link.click()






