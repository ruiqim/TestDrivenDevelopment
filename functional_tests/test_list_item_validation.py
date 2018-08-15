from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to the home page and accidentally tries to submit
        # an empy list item

        # The home page refreshes, and there is an error message saying that list
        # items can not be blank

        # User tries again with some text for the item, which now works

        # User tries to submit a second blank item

        # Receives the same warning on the list page

        # User can correct it by filling some text
        self.fail('write me!')
