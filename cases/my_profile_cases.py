import os

from cases.base_cases import Test
from pages.profile_page import ProfilePage
from pages.main.events_page import EventsPage

GEO_ERROR = 'Ошибка при определении местоположения'


class ProfileTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.login()

    def test_download_preview_picture(self):
        # Клик по кнопке загрузки аватара загружает картинку, показывает превью.
        new_avatar_path = os.path.join(os.getcwd(), 'img', 'new_avatar.jpeg')
        self.page.open()

        old_avatar_url = self.page.get_avatar_url()

        self.page.send_file(self.page.change_avatar, new_avatar_path)

        new_avatar_dataurl = self.page.get_avatar_url()

        print(old_avatar_url);
        print(new_avatar_dataurl);

        self.assertNotEqual(old_avatar_url, new_avatar_dataurl)

