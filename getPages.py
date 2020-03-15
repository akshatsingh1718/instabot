from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys as keys
import requests
import time 


# time halt between each  operation
TIME_INTERVAL = 2

class GetPages():
    # making LIKE_TIME_INTERVAL global 
    global TIME_INTERVAL 

    # GetPages constructor 
    def __init__(self, driver, username):
        self.driver = driver
        self.username = username


    # closing popup's
    def close_popup(self):
        # closing popup
        close_popup = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg > path')
        close_popup.click()


    def close_photos_window(self):
        # closing photo popup
        close_window = self.driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > svg')
        close_window.click()


    # extracting no of posts followers and folllowing
    def no_of_posts_followes_following(self):
        profile_bar = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul')))
        items = profile_bar.text.split('\n')
        for item in items:
            print(">> " + item)


    # like one post only
    def like_photo(self):
        # implict wait for like post
        self.driver.implicitly_wait(10)
        # liking photo
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()


    # fun for clicking on first post
    def click_on_first_post(self):
        self.driver.implicitly_wait(10)
        # clicking on 1st post
        self.driver.find_element_by_class_name('_9AhH0').click()


    # clicking on arrow to go on next post
    def  goto_next_post(self):
        self.driver.find_element_by_css_selector('div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow').click()


    # checking whether post is already liked or not
    def is_liked(self):
        self.driver.implicitly_wait(10)
        heart = self.driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')
        label = heart.get_attribute('aria-label')
        if label == 'Unlike':
            return True
        return False


    # check if the person account is private or not
    # returns true if account is private 
    def is_private(self):
        try:
            # checking for private label in account's profile
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div/h2')
        except NoSuchElementException:
            return False
        return True


    # check if page exist or not
    # return True if exist and vice-versa
    def is_page_exist(self):
        #self.driver.get("https://www.instagram.com/"+ page_name + '/')
        try:
            # checking for Account exist or not
            # basically checking for "Sorry, this page isn't available."
            self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/h2')
        except NoSuchElementException:
            return True
        return False


    # open page_name
    def get_page(self, page_name):
        print('>> opening '+ page_name +' profile...')
        # making page_name as class variable
        self.page_name = page_name

        self.driver.get("https://www.instagram.com/"+ page_name + '/')


    # fun for playing story
    def play_story(self, name):
        self.driver.implicitly_wait(10)
        # clicking on profile picture of account to play story
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span').click()


    # function to return comment box element
    def get_comment_area(self):
        self.driver.implicitly_wait(10)
        # returning comment box element 
        return self.driver.find_element_by_class_name('Ypffh')

    # function to return post button element
    def get_post_btn(self):
        # returning post button element
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')


    # auto commenting on post's
    def comment_on_photos(self, amount, comment):
        print('auto typing comment..')
        # clicking on first post of current page
        self.click_on_first_post()
        i = 0
        while(i <= amount):
            time.sleep(TIME_INTERVAL)

            '''
            I believe it has something to do with how instagram updates the textArea after you click on it, but this solution worked for me after searching and lots of trial and error
            '''
            # sending comment 
            comment_area = self.get_comment_area()
            comment_area.click()
            comment_area = self.get_comment_area()
            comment_area.send_keys(comment)

            # clicking on post button
            self.get_post_btn().click()

            i = i+1
            if(i == amount):
                break
            try:
                # click on right arrow to go to next post
                self.goto_next_post()
            except NoSuchElementException:
                break
        # closing popup
        self.close_photos_window()


    # like photos
    # amount is for no of posts to like
    def like_photos(self, amount):
        print(">> liking phosts..")
        # clicking on first post of current page
        self.click_on_first_post()
        
        i = 0
        while(i <= amount):
            time.sleep(TIME_INTERVAL)

            # if post is not already liked 
            if not self.is_liked():
                # liking photo
                self.like_photo()
                i = i+1
                if(i == amount):
                    break
            try:
                # click on right arrow to go to next post
                self.goto_next_post()
            except NoSuchElementException:
                break
        # closing popup
        self.close_photos_window()
        print(">> All photo's liked..")
    

    # open hashtag
    def get_hashtag(self, hashtag):
        print('opening '+ hashtag + "..")
        # assigning hashtag as class variable
        self.hashtag = hashtag
        # opening hashtag page
        self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag +'/')

    
    #get followers (public function)
    # returns unfollowers list
    def get_unfollowers(self):  
        print('getting unfollowers..') 
        # input page following button driver
        following_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
        By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
        following_button.click()

        # list of following names
        following = self.__get_names()

        # input page followers button driver
        followers_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
        By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
        followers_button.click()

        # list of following names
        followers = self.__get_names()

        # unfollowers list
        unfollowers = [name for name in following if name not in followers]
        # returning unfollowers list
        return unfollowers


    # __get_names (private function)
    # returns followers/following names as list
    def __get_names(self):
        try:
            # input page followers/following popup driver
            popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div.isgrP')))
            #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)

            # scrolling down to the bottom of popup
            old_ht , new_ht = 0, 1
            while old_ht != new_ht:
                old_ht = new_ht
                time.sleep(1)
                # running javascript to return height of scroll bar
                new_ht = self.driver.execute_script('''
                        arguments[0].scrollTo(0, arguments[0].scrollHeight)
                        return arguments[0].scrollHeight;''', popup)

            # getting links of all the a tags in popup 
            links = popup.find_elements_by_tag_name("li")
            names = [name.text.split('\n')[0] for name in links if name.text != '']
        #<><><>   StaleElementReferenceException   <><><>
        #Stale means old, decayed, no longer fresh. Stale Element means an old element or no longer available element. Assume there is an #element that is found on a web page referenced as a WebElement in WebDriver. If the DOM changes then the WebElement goes stale. If we #try to interact with an element which is staled then the StaleElementReferenceException is thrown.
        except StaleElementReferenceException:
            names = ''

        # closing popup
        self.close_popup()

        # returning followers/following names
        return names

        