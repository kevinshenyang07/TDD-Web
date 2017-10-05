from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A user land on the index page
        self.browser.get('http://localhost:8000')

        # The user notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        # fails the test anyway
        self.fail('Finish the test!')

        # The user is invited to enter a to-do item straight away

        # The user types "Buy peacock feathers" into a text box

        # There is still a text box inviting her to add another item. The user
        # enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then the user sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # The user visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main()


