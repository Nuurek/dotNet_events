from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_url = 'localhost:8000'

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()
