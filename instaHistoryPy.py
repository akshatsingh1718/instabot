from selenium import webdriver
from datetime import datetime
from collections import deque

class instaHistory():
    def __init__(self, driver):
        self.historys = deque()
        self.driver = driver
        
    # fun to get current date and time in string format
    def get_current_date_time(self):
        now = datetime.now()
        return now

    # fun to get current page url
    def get_current_page_url(self):
        url = self.driver.current_url
        return url

    # recording history
    def record_history(self, task):
        curr_url = self.get_current_page_url()
        curr_datetime = self.get_current_date_time()
        history = task + "\t" +  curr_url + "\t"  + str(curr_datetime)
        self.historys.appendleft(history)
        # self.historys.appendleft(f"{task} \t {curr_url} \t ")

    # displaying history
    def display_history(self):
        if self.historys:
            for history in self.historys:
                print(">> " + history)
        else:
            print(">> NO HISTORY..")

        
