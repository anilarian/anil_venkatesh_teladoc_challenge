import random

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


class AddUserPage(BasePage):
    F_NAME = (By.XPATH, F_NAME_XPATH)
    U_NAME = (By.XPATH, U_NAMR_XPATH)
    R_SELECT = (By.XPATH, R_SELECT_XPATH)
    PH_NUM = (By.XPATH, PH_NUM_XPATH)
    ADD_SUBMIT = (By.XPATH, ADD_SUBMIT_XPATH)
    ADD_USER = (By.XPATH, ADD_USER_XPATH)

    def add_user(self, f_name, u_name, ph_num):
        # self.do_click(self.ADD_USER)
        self.do_send_keys(self.F_NAME, f_name)
        self.do_send_keys(self.U_NAME, u_name)
        self.do_select_value(self.R_SELECT, random.randint(0, 2))
        self.do_send_keys(self.PH_NUM, ph_num)
        self.do_click(self.ADD_SUBMIT)
