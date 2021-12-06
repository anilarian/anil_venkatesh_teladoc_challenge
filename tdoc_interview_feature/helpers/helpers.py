"""Helpers functions for interacting with webtabbles page"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

email_domain = '@tdocinterview.com'


class UserRoles:
    sales_team = 'Sales Team'
    customer = 'Customer'
    Admin = 'Admin'


def build_user_email(f_name: str):
    return f_name + email_domain


def build_user_name(f_name: str):
    return f_name[:4]


def add_user_details(driver, f_name):
    driver.find_elements(By.XPATH, '/html/body/table/thead/tr[2]/td/button')[0].click()
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input')[0].send_keys('Anil')

    select = Select(driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[6]/td[2]/select/]')[0])
    select.select_by_value('{}'.format(random.randint(1, 3)))

    driver.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input')[0].send_keys('{}'.format(random.randint(100, 300)))
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[3]/button[2]')[0].click()

