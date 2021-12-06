"""Base page actions module."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_xpath)).click()

    def do_send_keys(self, by_xpath, keys):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_xpath)).send_keys(keys)

    def get_element(self, by_xpath):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_xpath))

    def do_select_value(self, by_xpath, value):
        select = Select(self.get_element(by_xpath))
        select.select_by_value('{}'.format(value))

    def find_in_smart_data_table(self, by_xpath, value):

        table = self.get_element(by_xpath)
        elements = table.find_elements(By.CLASS_NAME, 'smart-table-data-row')
        for element in elements:
            data_row = element.find_elements(By.CLASS_NAME, 'smart-table-data-cell')
            for data_col in data_row:
                if data_col.accessible_name == value:
                    print('User {} successfully added into web table'.format(value))
                    return data_row
        return False
