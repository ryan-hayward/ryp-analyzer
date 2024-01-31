# set up demo connection to a browser with selenium
import time
import requests
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# set up general config parser
config = configparser.ConfigParser()
config.read('config.ini')

def login(url: str):
    # set up the selenium web driver and connect to RYP
    driver = webdriver.Chrome()
    driver.get(url)

    # get email and password from config file
    # @TODO seet up automation for the config file
    email = config['LOGIN']['email']
    password = config['LOGIN']['password']

    # input email and press button to continue
    input_email = driver.find_element(By.NAME, 'id')
    input_email.send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/form/div[4]/button').click()

    # input password and press button to continue
    input_pw = driver.find_element(By.NAME, 'password')
    input_pw.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/form/div[3]/button').click()

    time.sleep(100)
    driver.quit()


def get_soup(request_url: str) -> BeautifulSoup:
    # store response from request
    response = requests.get(request_url)
    # return soup
    return BeautifulSoup(response.text, 'html.parser')


def main():
    login('https://www.runyourpool.com/auth/sign-in/')
    #soup = get_soup('https://www.runyourpool.com/NFL/Fantasy/Reports/standings.cfm')
    #input_field = soup.find('input')
    #print(input_field)

if __name__ == '__main__':
    main()