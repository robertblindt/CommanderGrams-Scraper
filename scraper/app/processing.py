import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# you also need to pip install webdriver_manager.  it shouldnt be in the requirments.txt
from webdriver_manager.chrome import ChromeDriverManager
from unidecode import unidecode


class Processing():
    # This module is the heart of the card word processing and database inserts.
    # The scrape procedure goes: 
    # User requests card => Processing cleans the input, Checks if the card is in the database, calls to EDHrec to scrape for cards related (Check if cards have been scraped within X days) => Processing reformats the names, checks if the card is already in the database, calls Scryfall to fill in cards that aren't already there => While inserting, a connection should be made in Commander_collections =>

    def _clean_search_input(self, card_name,use):
        # 0 for EDH Rec end points, 1 (or anything) for Scryfall '+' joined for Scryfalls fuzzy search
        # print(card_name)
        if '//' in card_name:
            card_name = card_name.split('//')[0]
        card_name = unidecode(card_name)
        card_name = card_name.replace("'", "")
        word_pat = re.compile("[A-Za-z]+")
        cleaned_input = re.findall(word_pat, card_name)
        if use == 0:
            return '-'.join(cleaned_input).lower()
        else:
            return '+'.join(cleaned_input).lower()

    def parseEDHrec_for_card_names(self, card_name):
        # FOR WORKING ON MY LOCAL MACHINE
        # service=Service(ChromeDriverManager().install())
        # For working on Docker container
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # options = Options()
        # options.add_argument("--no-sandbox")
        # options.add_argument("--headless")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--verbose") 
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-features=dbus")
        # log_path = "{}/chromedriver.log".format('/app')
        # service_args = ['--no-sandbox', '--headless','--disable-dev-shm-usage', '--verbose']
        # service = webdriver.chrome.service.Service(executable_path='/usr/local/bin/chromedriver-linux64/chromedriver', service_args = service_args, log_path=log_path)    
        # driver = webdriver.Chrome(options=options, service=service)

        url = f'https://edhrec.com/commanders/{self._clean_search_input(card_name,0)}'
        # driver.implicitly_wait(10)
        print(driver)
        driver.get(url)
        time.sleep(3)

        if driver.find_elements(By.CLASS_NAME, 'page-heading')[0].text == 'Error 403':
            print('Could not find Commander.  Please check your spelling!')
            driver.close()
            return None
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        y = 1000
        prev_pos = 0
        # I need to scroll through the page in order to load all the card tags so I can grab the card names.
        for timer in range(0,70):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            
            current_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            # This should break when the page gets to the bottom instead of going for the full 7
            # Selenium is a bit slow and laggy, so this only helps so much.
            if current_scroll_height < y:
                #print('breaking')
                break  

            y += 1000 
            # print('scrolling')
            time.sleep(.1)
            
        page_card_cont = []
        for i in driver.find_elements(By.TAG_NAME, 'a'):
            if i.get_attribute('href').split('/')[-2] == 'cards':
                page_card_cont.append(i.get_attribute('href').split('/')[-1])
        driver.close()
        # Add the commander to the list of card to pull. Need to also add a Database insert here!
        page_card_cont.append(self._clean_search_input(card_name,0))
        print(set(page_card_cont))
        return set(page_card_cont)
    

    def parseEDHrec_for_commanders(self, page_type):      
        # FOR WORKING ON MY LOCAL MACHINE
        # service=Service(ChromeDriverManager().install())
        # For working on Docker container
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # options = Options()
        # options.add_argument("--no-sandbox")
        # options.add_argument("--headless")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--verbose") 
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-features=dbus")
        # log_path = "{}/chromedriver.log".format('/app')
        # service_args = ['--no-sandbox', '--headless','--disable-dev-shm-usage', '--verbose']
        # service = webdriver.chrome.service.Service(executable_path='/usr/local/bin/chromedriver-linux64/chromedriver', service_args = service_args, log_path=log_path)    
        # driver = webdriver.Chrome(options=options, service=service)
        
        if page_type == 1:
            url = 'https://edhrec.com/commanders/year'
        elif page_type == 2:
            url = 'https://edhrec.com/commanders/month'
        # For some reason Week opens the week page, but get the year data...
        elif page_type == 3:
            url = 'https://edhrec.com/commanders/week'
        else:
            print("Only enter 'long'(default), 'month', or 'week'")
            
        # driver.implicitly_wait(10)
        driver.get(url)
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        y = 1000
        prev_pos = 0
        # I need to scroll through the page in order to load all the card tags so I can grab the card names.
        for timer in range(0,70):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            
            current_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            # This should break when the page gets to the bottom instead of going for the full 7
            # Selenium is a bit slow and laggy, so this only helps so much.
            if current_scroll_height < y:
                #print('breaking')
                break  
                
            y += 1000 
            # print('scrolling')
            time.sleep(.1)
            
        page_card_cont = []
        for i in driver.find_elements(By.CLASS_NAME, 'Card_name__vpWb5'):
            if ' // ' in i.text:
                page_card_cont.append(i.text.split(' // ')[0])
            else:
                page_card_cont.append(i.text)
        driver.close()
        return set(page_card_cont)