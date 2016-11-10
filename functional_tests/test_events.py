from .base import FunctionalTest

PAGE_TITLE = '.NET events'


class NewVisitorTest(FunctionalTest):

    def test_can_see_all_home_page_elements(self):
        # Jacob got message from .NET leader to try out new page project.
        # He goes to check out its homepage on localhost.
        print(self.server_url)
        self.browser.get(self.server_url)

        # He notices the page title and header mention .NET events
        self.assertIn(PAGE_TITLE, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(PAGE_TITLE, header_text)

        # There is also a button for logging in.

        # And the largest from them all: schedule showing all upcoming events
        # for one of the .NET groups.
