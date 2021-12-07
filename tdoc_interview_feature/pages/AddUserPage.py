"""Add user page functional interface."""

import random

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages import constants


class AddUserPage(BasePage):
    F_NAME = (By.XPATH, constants.F_NAME_XPATH)
    U_NAME = (By.XPATH, constants.U_NAMR_XPATH)
    R_SELECT = (By.XPATH, constants.R_SELECT_XPATH)
    PH_NUM = (By.XPATH, constants.PH_NUM_XPATH)
    ADD_SUBMIT = (By.CLASS_NAME, 'btn-success')
    ADD_USER = (By.XPATH, constants.ADD_USER_XPATH)

    def add_user(self, f_name, u_name, ph_num):
        self.do_send_keys(self.F_NAME, f_name)
        self.do_send_keys(self.U_NAME, u_name)
        self.do_select_value(self.R_SELECT, random.randint(0, 2))
        self.do_send_keys(self.PH_NUM, ph_num)
        self.do_click(self.ADD_SUBMIT)
