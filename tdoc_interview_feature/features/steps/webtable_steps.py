""" Steps needed for web tables automation feature."""

import logging

from behave import *
from selenium import webdriver

from pages import (
    AddUserPage,
    MainPage,
    constants
)


# TODO: Use fixtures to setup web driver.
@given('Launch chrome browser')
def launch_chrome_browser(context):
    logging.info("Initializing the chrome web driver")
    context.driver = webdriver.Chrome()


@when('Web tables page is opened')
def open_web_page(context):
    logging.info("Navigate to webpage and initialize POMs")
    context.driver.get(constants.WEB_TABLES)
    context.main_page = MainPage(context.driver)
    context.add_user_page = AddUserPage(context.driver)


@then('Add user f_name: "{f_name}" u_name: "{u_name}" ph_num: "{ph_num}" to the table')
def add_user(context, f_name, u_name, ph_num):
    logging.info('Add user f_name: {} u_name: {} ph_num: {} to the table'.format(f_name, u_name, ph_num))
    context.main_page.add_user_click()
    context.add_user_page.add_user(f_name, u_name, ph_num)


@then('Validate the user f_name: "{f_name}" has been added to the table')
def verify_added(context, f_name):
    logging.info('Verify user firstname: {} was added to the table'.format(f_name))
    if context.main_page.find_user_in_table(f_name):
        logging.info('User firstname: {} was found in the table'.format(f_name))
    else:
        assert False, 'User not added'


@then('Delete a User u_name: "{u_name}" from the table')
def step_impl(context, u_name):
    logging.info('Find user Username: {} and delete user'.format(u_name))
    context.main_page.find_user_and_delete(u_name)


@then('Validate the user u_name: "{u_name}" has been deleted')
def step_impl(context, u_name):
    if context.main_page.find_user_in_table(u_name):
        assert False, 'user Username: {} Not deleted'.format(u_name)
    else:
        logging.info('user Username: {} successfully deleted'.format(u_name))


@then('close the browser')
def close_browser(context):
    context.driver.close()
