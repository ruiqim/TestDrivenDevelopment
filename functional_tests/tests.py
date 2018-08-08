from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):

        # User goes to homepage:

        self.browser.get(self.live_server_url)

        # User checks that page title and header display to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is asked to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types "Buy Groceries"
        inputbox.send_keys("Buy Groceries")
        # When user hits enter, the page lists
        # "1: Buy Groceries" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy Groceries')

        # The text box remains, asking to enter another item.
        # User enters another item "Cook Dinner"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Cook Dinner")
        inputbox.send_keys(Keys.ENTER)
        # Page updates again and now shows both items on list
        self.wait_for_row_in_list_table('1: Buy Groceries')
        self.wait_for_row_in_list_table('2: Cook Dinner')

        # User notices that site has generate a unique url

        # User visits url and sees list is still there

        # User Quits the browser
        self.fail('Finish the Test!')
