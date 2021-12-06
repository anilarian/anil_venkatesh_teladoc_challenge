from _ast import And

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time

ADD_USER_XPATH = '/html/body/table/thead/tr[2]/td/button'
F_NAME_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input'
U_NAMR_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input'
R_SELECT_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[6]/td[2]/select'
PH_NUM_XPATH = '/html/body/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input'
ADD_SUBMIT_XPATH = '/html/body/div[3]/div[3]/button[2]'
USER_TABLE_XPATH = '/html/body/table/tbody'
OK_BTN_XPATH = '/html/body/div[3]/div[3]/button[2]'


@given('Launch chrome browser')
def launch_chrome_browser(context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    context.driver = webdriver.Chrome(chrome_options=options)


@when('Webtables page is opened')
def open_web_page(context):
    context.driver.get('http://www.way2automation.com/angularjs-protractor/webtables/')
    time.sleep(5)


@then('Add user f_name: "{f_name}" u_name: "{u_name}" ph_num: "{ph_num}" to the table')
def add_user(context, f_name, u_name, ph_num):
    # Find element by xpath and click add user button
    context.driver.find_elements(By.XPATH, ADD_USER_XPATH)[0].click()
    # time.sleep(5)

    # Find element by xpath and send f_name value to the input box
    context.driver.find_elements(By.XPATH, F_NAME_XPATH)[0].send_keys(f_name)
    # time.sleep(5)
    # Find element by xpath and send u_name value to the input box
    context.driver.find_elements(By.XPATH, U_NAMR_XPATH)[0].send_keys(u_name)
    # time.sleep(5)
    # Find element by xpath, create a select object and select a random value for role
    select = Select(context.driver.find_elements(By.XPATH, R_SELECT_XPATH)[0])
    select.select_by_value('{}'.format(random.randint(0, 2)))

    # Find element by xpath and send phone number value to the input box
    context.driver.find_elements(By.XPATH, PH_NUM_XPATH)[0].send_keys(ph_num)

    # Find element by xpath and click submit form
    context.driver.find_elements(By.XPATH, ADD_SUBMIT_XPATH)[0].click()


@then('Validate the user f_name: "{f_name}" has been added to the table')
def verify_added(context, f_name):
    table = context.driver.find_elements(By.XPATH, USER_TABLE_XPATH)[0]
    elements = table.find_elements(By.CLASS_NAME, 'smart-table-data-row')
    for element in elements:
        data_rows = element.find_elements(By.CLASS_NAME, 'smart-table-data-cell')
        for data_col in data_rows:
            if data_col.accessible_name == f_name:
                print('User {} successfully added into web table'.format(f_name))
                return True
    assert False, 'User not found in web table'


@then('Delete a User u_name: "{u_name}" from the table')
def step_impl(context, u_name):
    table = context.driver.find_elements(By.XPATH, USER_TABLE_XPATH)[0]
    elements = table.find_elements(By.CLASS_NAME, 'smart-table-data-row')
    for element in elements:
        data_rows = element.find_elements(By.CLASS_NAME, 'smart-table-data-cell')
        for data_col in data_rows:
            if data_col.accessible_name == u_name:
                print('User {} found in web table, deleting now'.format(u_name))
                delete_button = data_rows[-1].find_elements(By.TAG_NAME,  'button')[0]
                delete_button.click()
                ok_button = context.driver.find_elements(By.XPATH, OK_BTN_XPATH)[0]
                ok_button.click()
                return True
    assert False, 'User not found in web table'


@then('Validate the user u_name: "{u_name}" has been deleted')
def step_impl(context, u_name):
    table = context.driver.find_elements(By.XPATH, USER_TABLE_XPATH)[0]
    elements = table.find_elements(By.CLASS_NAME, 'smart-table-data-row')
    for element in elements:
        data_rows = element.find_elements(By.CLASS_NAME, 'smart-table-data-cell')
        for data_col in data_rows:
            if data_col.accessible_name == u_name:
                return False, 'User {} found in web table'.format(u_name)
    assert True, 'User successfully deleted from webtable'



@then('close the browser')
def close_browser(context):
    context.driver.close()
