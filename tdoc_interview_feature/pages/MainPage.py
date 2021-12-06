from selenium.webdriver.common.by import By
from tdoc_interview_feature.pages.BasePage import BasePage

ADD_USER_XPATH = '/html/body/table/thead/tr[2]/td/button'
F_NAME_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input'
U_NAMR_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input'
R_SELECT_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[6]/td[2]/select'
PH_NUM_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input'
ADD_SUBMIT_XPATH = '/html/body/div[3]/div[3]/button[2]'
USER_TABLE_XPATH = '/html/body/table/tbody'
OK_BTN_XPATH = '/html/body/div[3]/div[3]/button[2]'
WEB_TABLES = 'http://www.way2automation.com/angularjs-protractor/webtables/'


class MainPage(BasePage):
    ADD_USER = (By.XPATH, ADD_USER_XPATH)
    USER_TABLE = (By.XPATH, USER_TABLE_XPATH)

    def __init__(self, driver):
        super().__init__(driver)

    def find_user_in_table(self, value):
        return self.find_in_smart_data_table(self.USER_TABLE, value)

    def find_user_and_delete(self, value):
        data_row = self.find_in_smart_data_table(self.USER_TABLE, value)
        delete_button = data_row[-1].find_elements(By.TAG_NAME, 'button')[0]
        delete_button.click()
        ok_button = self.driver.find_elements(By.XPATH, OK_BTN_XPATH)[0]
        ok_button.click()

    def add_user_click(self):
        self.do_click(self.ADD_USER)
