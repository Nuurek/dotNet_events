from .base import FunctionalTest

PAGE_TITLE = '.NET events'
NEW_SCHEDULE_BUTTON_TEXT = 'Create new schedule'

class NewVisitorTest(FunctionalTest):

    def test_can_see_all_home_page_elements(self):
        # Jacob got message from .NET leader to try out new page project.
        # He goes to check out its homepage on localhost.
        print(self.server_url)
        self.browser.get(self.server_url)

        # He notices the page title and header mention .NET events
        self.assertIn(PAGE_TITLE, self.browser.title)
        brand_text = self.browser.find_element_by_css_selector('.brand').text
        self.assertIn(PAGE_TITLE, brand_text)

        # There's also navbar on the top of the site
        navbar_items = self.browser.find_elements_by_css_selector('.nav-item')
        self.assertNotEqual(len(navbar_items), 0)

        # And the largest from all elements:
        # schedule showing all upcoming events for one of the .NET groups.
        schedule = self.browser.find_element_by_id('events-window')

        # Beneath the schedule there's a button located.
        new_button = self.browser.find_element_by_id('new-schedule-button')
        self.assertEqual(NEW_SCHEDULE_BUTTON_TEXT, new_button.text)
