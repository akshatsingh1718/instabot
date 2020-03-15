from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import loginPy
import instaHistoryPy
import getPages
#play story
'''
    pip install lxml
'''

# driver as global variable
driver = 0
username = 'mynameisgod1718@gmail.com'
password = 'Mynameisgod1718@'

def main():
    global driver
    print('running script.......')
    driver = webdriver.Chrome('E:\\python\\ChromeDriver\\chromedriver.exe')
    # for maximizing window
    driver.maximize_window()
    # login page object
    login = loginPy.Login(username, password, driver)
    login.signin()
    history = instaHistoryPy.instaHistory(driver)

    # GetPages object
    gp = getPages.GetPages(driver, username)
    
    # menu created as dictionary
    menu ={
        1:"Open My Profile",
        2:"Open Others Profile",
        3:"Get Unfollowers List",
        4:"Get Other's Unfollowers List",
        5:"Auto Like Posts",
        6:"Auto Like HashTags",
        7:"Auto comment on people",
        8:"Auto comment on hashtag",
        9:"Get No of Posts ,followers and following",
        10:"Play Stories",
        11:"History",
    }

    while(1):
        print("###########################################################")
        print("\t\tINSTAGRAM BOT")
        print("###########################################################")

        # displaying menu using dictionaries 
        for i in range(1,len(menu)+1):
            print(str(i) + ". " +  menu[i])
        print("0.Exit")

        try:
            opt = int(input("[Instagram@Bot]#"))
        except ValueError :
            print("No valid option entered !")
            continue

    # opening user's profile
        if opt == 1:
            # username slicing for removing '@gmail.com' from the end
            driver.get("https://www.instagram.com/"+ username[0:-10] +'/')

    # opening others profile
        elif opt == 2:
            target_name = input("Enter profile username to open :")
            gp.get_page(target_name)
            if not gp.is_page_exist():
                print(target_name + " does not exist")
            elif gp.is_private():
                print(target_name + " is Private Account")

    # getting user's unfollowers list
        elif opt == 3:
            gp.get_page(username[0:-10])
            unfollowers = gp.get_unfollowers()
            print("----- Unfollowers -----")
            print(unfollowers)
            print(">> "+ len(unfollowers) + " unfollowers found..")

    # getting target person unfollowers list account if it's not private account
        elif opt == 4:
            target_name = input("Enter target name to find its unfollowers :")
            # opening target page
            gp.get_page(target_name)
            # cehcking is the user input account exist or not
            if gp.is_page_exist():
                #  checking if it's private or not
                if  gp.is_private() == False:
                    unfollowers = gp.get_unfollowers()
                    print("----- Unfollowers -----") 
                    print(unfollowers)
                    print(">> "+ len(unfollowers) + " unfollowers found..")
                else:
                    print(target_name + " is private account")
            else:
                print(target_name + " does not exist")

    # liking people's post
        elif opt == 5:
            target_name = input("Enter target's name to like :@")
            gp.get_page(target_name)
            if gp.is_page_exist():
                if not gp.is_private():
                        # loop for checking if user input is an integer or not
                        # and if it's an integer then call like_photos fun
                        while True:
                            try:
                                no_of_post_to_like = int(input("Enter no of post to like:"))   
                                gp.like_photos(no_of_post_to_like)
                            except ValueError:
                                print('WRONG VALUE ENTERED!')
                                continue
                            # break loop if user input right value
                            break
                else:
                    print(">> " + "cannot like target posts...")
                    print(">> " + target_name + " is private account")
            else:
                print(">> " + target_name + " does not exist")

    # liking hashtag post
        elif opt == 6:
            hashtag = input("Enter hashtag page name to like posts :#")
            gp.get_hashtag(hashtag)
            if gp.is_page_exist():
                # loop for checking if user input is an integer or not
                # and if it's an integer then call like_photos fun
                while True:
                    try:
                        no_of_post_to_like = int(input("Enter no of post to like:"))   
                        gp.like_photos(no_of_post_to_like)
                    except ValueError:
                        print('WRONG VALUE ENTERED!')
                        continue
                    # break loop if user input right value
                    break
            else:
                print(">> #" + hashtag + " does not exist")

    # auto comment on target's posts
        elif opt == 7:
            target_name = input("Enter target's name on which you want to comment on :@")
            gp.get_page(target_name)
            if gp.is_page_exist():
                if not gp.is_private():
                        # loop for checking if user input is an integer or not
                        # and if it's an integer then call comment_on_photos fun
                        while True:
                            try:
                                no_of_post_to_cmt = int(input("Enter no of post you want to comment on :"))   
                                cmt = input("Enter your text you want to comment :")
                                gp.comment_on_photos(no_of_post_to_cmt, cmt)
                            except ValueError:
                                print('WRONG VALUE ENTERED!')
                                continue
                            # break loop if user input right value
                            break
                else:
                    print(">> " + "cannot comment on target's posts...")
                    print(">> " + target_name + " is private account")
            else:
                print(">> " + target_name + " does not exist")

    # auto comment on target hashtag post
        elif opt == 8:
            hashtag = input("Enter hashtag page name you want to comment on :#")
            gp.get_hashtag(hashtag)
            if gp.is_page_exist():
                # loop for checking if user input is an integer or not
                # and if it's an integer then call like_photos fun
                while True:
                    try:
                        no_of_post_to_cmt = int(input("Enter no of post you want to comment on :"))  
                        cmt = input("Enter your text you want to comment :")
                        gp.comment_on_photos(no_of_post_to_cmt, cmt)

                    except ValueError:
                        print('WRONG VALUE ENTERED!')
                        continue
                    # break loop if user input right value
                    break
            else:
                print(">> #" + hashtag + " does not exist")     

    # print no of posts, followers and following
        elif opt == 9:
            target_name = input("Enter target's name to fetch information :@")
            gp.get_page(target_name)
            if gp.is_page_exist():
                gp.no_of_posts_followes_following()
            else:
                print(">> " + target_name + " does not exist")

    # play target person's story
        elif opt == 10:
            target_name = input("Enter target's name to show it's story :@")
            gp.get_page(target_name)
            if gp.is_page_exist():
                if not gp.is_private():  
                    gp.play_story(target_name)
                else:
                    print(">>ERROR : " + "cannot show story of  Private Account")
            else:
                print(">> " + target_name + " does not exist")
   
    # display history
        elif opt == 11:
            print("\t\tInstagram History")
            history.display_history()

    # exit program
        elif opt == 0:
            print("Exiting InstaBot")
            driver.execute_cdp_cmd
            exit()

    # if option is no found in menu
        else:
            print(">> Invalid input")    

        # recoring history
        history.record_history(menu[opt])



'''
    ############# M A I N ############
'''
if __name__ == '__main__':
    main()

    