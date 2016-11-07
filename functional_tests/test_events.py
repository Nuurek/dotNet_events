from .base import FunctionalTest

PAGE_TITLE = '.NET events'
NEW_SCHEDULE_BUTTON_TEXT = 'Create new schedule'


class NewVisitorTest(FunctionalTest):

    def test_can_start_new_event(self):
        # Jacob got message from .NET leader to try out new page project
        # He goes to check out its homepage on localhost
        print(self.server_url)
        self.browser.get(self.server_url)

        # He notices the page title and header mention .NET events
        self.assertIn(PAGE_TITLE, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(PAGE_TITLE, header_text)

        # There is also a large button prompting to start new schedule
        new_schedule_button_text = self.browser.find_element_by_id(
                                        'new-schedule-button').text
        self.assertIn(NEW_SCHEDULE_BUTTON_TEXT, new_schedule_button_text)
