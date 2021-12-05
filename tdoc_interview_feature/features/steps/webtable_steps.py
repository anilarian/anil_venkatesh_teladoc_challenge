from _ast import And

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time


@given('Launch chrome browser')
def launch_chrome_browser(context):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    context.driver = webdriver.Chrome(chrome_options=options)


@when('Webtables page is opened')
def open_web_page(context):
    context.driver.get('http://www.way2automation.com/angularjs-protractor/webtables/')


@then('Add users to the table')
def add_user(context):
    context.driver.find_elements(By.XPATH, '/html/body/table/thead/tr[2]/td/button')[0].click()
    time.sleep(5)
    context.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input')[0].send_keys(
        'Anil')
    time.sleep(5)
    context.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input')[0].send_keys(
        'Anil')
    time.sleep(5)
    select = Select(
        context.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[6]/td[2]/select')[0])
    select.select_by_value('{}'.format(random.randint(0, 2)))
    time.sleep(5)
    context.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input')[0].send_keys(
        '{}'.format(random.randint(100, 300)))
    time.sleep(5)
    context.driver.find_elements(By.XPATH, '/html/body/div[3]/div[3]/button[2]')[0].click()
    time.sleep(5)


@then('Validate the user has been added to the table')
def verify_added(context):
    table = context.driver.find_elements(By.XPATH, '/html/body/table/tbody')[0]
    elements = table.find_elements(By.CLASS_NAME, 'smart-table-data-row')
    for element in elements:
        data_rows = element.find_elements(By.CLASS_NAME, 'smart-table-data-cell')
        for data_col in data_rows:
            if data_col.accessible_name == 'Anil':
                print('User {} successfully added into web table')
                return True
    assert False, 'User not added into web table'


@then('close the browser')
def close_browser(context):
    context.driver.close()
