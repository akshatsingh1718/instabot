from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time 

class Login():
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def signin(self):
        print('opening Instagram....')
        self.driver.get('https://www.instagram.com/')

        # username button element
        user_name_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')))
        user_name_button.click()
        user_name_button.send_keys(self.username)

        # password button element
        password_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password_button.click()
        password_button.send_keys(self.password)

        # login button element
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        login_button.click()

        # if Turn on Notifications pop appear
        not_now = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
        By.XPATH,'/html/body/div[4]/div/div/div[3]/button[2]')))
        not_now.click()