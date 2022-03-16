# SLICS automation
# http://leidos.unanet.biz/leidos/action/home

from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time



page = 'https://leidos.unanet.biz/leidos/action/home'

#webbrowser.open(page)
driver.get(page)

uname = input("Enter Username: ")
pword = input("Enter Password: ")


elem = driver.find_element_by_id('username').send_keys(uname)
time.sleep(1.5)
elem = driver.find_element_by_id('password').send_keys(pword)
time.sleep(1)

# Click login
driver.find_element_by_xpath('//*[@id="button_ok"]').click()
time.sleep(1.2)

#navigate to the queue
driver.find_element(by=By.XPATH, value='//*[@id="body"]/table/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/a').click()

# Select the first record
# records = len(driver.find_elements_by_xpath('/html/body/div[3]/form/div[1]/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/a'))
record = driver.find_element(by=By.XPATH, value='/html/body/div[3]/form/div[1]/div[2]/div[2]/div[2]/table/tbody[2]/tr[1]/td[1]/a').click()
time.sleep(2)

def loop():
    
    while True:
        print('1. Running...')
        # time.sleep(2)
        #get the current record title
        current_record_title = driver.find_element(by=By.XPATH, value='//*[@id="title-subsection"]').text
        print('2. ' + current_record_title)
            
        t_time = driver.find_element(by=By.CSS_SELECTOR, value='#approval-body > div.timesheet > table > tfoot > tr > td.total').text
        t_time = float(t_time)
        t_time_str = str(t_time)
        print('3. '+t_time_str)
        
        # Grab the approval history table
        l = driver.find_elements(by=By.XPATH, value='/html/body/div[3]/div/div[3]/table/tbody/tr')
                
        # Get the value of the last row in the approval history table
        l = l[-1].text
        
        # Define the approve button
        approve = driver.find_element(by=By.XPATH, value='//*[@id="button_approve_next"]')
        # Define the skip button
        skip = driver.find_element(by=By.XPATH, value='//*[@id="button_skip"]')
        print('4. ' + l)
        
        #if 
        if t_time <= 40.00 and "APPROVING" in l and 'Duncan' not in l and 'Malm' not in l:
            print('Hours are 40 or under, \n it\'s already approved by the manager, \n and it\'s not Jason Malm! \n All Looks Good!')
            approve.click()
        else:
            print('Not Approving')
            print('Skipping...')
            #time.sleep(2)
            skip.click()   
                    
        record_title = driver.find_element(by=By.XPATH, value='//*[@id="title-subsection"]').text
        if current_record_title == record_title:
            break
        else:
            pass
        
        
        
                


    
