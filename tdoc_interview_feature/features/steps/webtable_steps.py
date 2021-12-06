""" Steps needed for web tables automation feature."""

from behave import *
from selenium import webdriver

from pages import (
    AddUserPage,
    MainPage,
)

WEB_TABLES = 'http://www.way2automation.com/angularjs-protractor/webtables/'


# TODO: Use fixtures to setup web driver.
@given('Launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome()


@when('Web tables page is opened')
def open_web_page(context):
    context.driver.get(WEB_TABLES)
    context.main_page = MainPage(context.driver)
    context.add_user_page = AddUserPage(context.driver)


@then('Add user f_name: "{f_name}" u_name: "{u_name}" ph_num: "{ph_num}" to the table')
def add_user(context, f_name, u_name, ph_num):
    context.main_page.add_user_click()
    context.add_user_page.add_user(f_name, u_name, ph_num)


@then('Validate the user f_name: "{f_name}" has been added to the table')
def verify_added(context, f_name):
    if context.main_page.find_user_in_table(f_name):
        print('success')
    else:
        assert False, 'User not added'


@then('Delete a User u_name: "{u_name}" from the table')
def step_impl(context, u_name):
    context.main_page.find_user_and_delete(u_name)


@then('Validate the user u_name: "{u_name}" has been deleted')
def step_impl(context, u_name):
    if context.main_page.find_user_in_table(u_name):
        assert False, 'User not deleted'
    else:
        print('Success')


@then('close the browser')
def close_browser(context):
    context.driver.close()
