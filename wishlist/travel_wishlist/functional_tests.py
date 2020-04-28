import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn(self.browser.title, 'Travel Wishlist')

class AddEditPlacesTests(LiveServerTestCase):

    fixtures = ['test_users', 'test_places']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):

        self.browser.get(self.live_server_url) # Load home page
        input_name = self.browser.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        add_button = self.browser.find_element_by_id('add-new-place')
        add_button.click()

        wait_for_denver = self.browser.find_element_by_id('place-name-5')

        self.assertIn('Tokyo', self.browser.page_source)
        self.assertIn('New York', self.browser.page_source)

        self.assertIn('Denver', self.browser.page_source)