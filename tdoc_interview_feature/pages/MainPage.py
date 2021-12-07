"""Main web tables page functional interface."""
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages import constants


class MainPage(BasePage):
    """Page object model for the Main page."""
    ADD_USER = (By.XPATH, constants.ADD_USER_XPATH)
    USER_TABLE = (By.XPATH, constants.USER_TABLE_XPATH)

    def __init__(self, driver):
        super().__init__(driver)

    # TODO: Extend this function to validate all updated values.
    def find_user_in_table(self, value):
        """Find a given value in smart data table and return the row it was found in. """
        return self.find_in_smart_data_table(self.USER_TABLE, value)

    def find_user_and_delete(self, value):
        """Find a given value in smart data table and delete the row. """
        data_row = self.find_in_smart_data_table(self.USER_TABLE, value)
        delete_button = data_row[-1].find_elements(By.TAG_NAME, 'button')[0]
        delete_button.click()
        self.do_click((By.XPATH, constants.OK_BTN_XPATH))

    def add_user_click(self):
        """Click add user. """
        self.do_click(self.ADD_USER)
