from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # User goes to homepage:

        self.browser.get('http://localhost:8000')

        # User checks that page title and header display to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')

        # User is asked to enter a to-do item

        # User types "Buy Groceries"

        # When user hits enter, the page lists
        # "1: Buy Groceries" as an item in a to-do list

        # The text box remains, asking to enter another item.
        # User enters another item "Cook Dinner"

        # Page updates again and now shows both items on list

        # User notices that site has generate a unique url

        # User visits url and sees list is still there

        # User Quits the browser

if __name__=='__main__':
    unittest.main(warnings='ignore')
