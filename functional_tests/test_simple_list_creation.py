from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):


    def test_can_start_a_list_for_one_user(self):

        # User goes to homepage:

        self.browser.get(self.live_server_url)

        # User checks that page title and header display to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is asked to enter a to-do item
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Cook Dinner")
        inputbox.send_keys(Keys.ENTER)
        # Page updates again and now shows both items on list
        self.wait_for_row_in_list_table('1: Buy Groceries')
        self.wait_for_row_in_list_table('2: Cook Dinner')

        # User notices that site has generate a unique url

        # User visits url and sees list is still there

        # User Quits the browser


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # User starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Groceries')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Groceries')

        # User notices that list has unique url
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url,'lists/.+')

        # User 2 loads page
        # Open new session

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # User 2 visits home page. There is no sign of User list`
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Groceries', page_text)
        self.assertNotIn('Cook Dinner', page_text)


        # User 2 starts a new list by entering a new item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Finish Homework')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Finish Homework')

        # User two gets a unique url
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url,'lists/.+')
        self.assertNotEqual(user_list_url,user2_list_url)

        # No trace of User list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Groceries', page_text)
        self.assertNotIn('Cook Dinner', page_text)
