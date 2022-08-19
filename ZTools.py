import random
import time
import os
import re
import uuid
from datetime import datetime
import requests

def code():
    try:
        import chromedriver_autoinstaller
        print("Chromedriver auto installer installed!")
    except:
        os.system("pip install chromedriver-autoinstaller")
    try:
        from selenium import webdriver
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.support import expected_conditions as EC
        print("Selenium has been installed.")
    except:
        os.system("pip3 install selenium")

    try:
        import undetected_chromedriver as uc
        print("Undetected Chromedriver has been installed.")
    except:
        os.system("pip3 install undetected-chromedriver")

    try:
        from webdriver_manager.chrome import ChromeDriverManager
        print("Webdriver Manager has been installed.")
    except:
        os.system("pip install webdriver-manager")

    try:
        from pypresence import Presence
        print("Pypresence has been installed.")
    except:
        os.system("pip install pypresence")

    # Try & Except, only when these libraries have not been installed on user computers will they only branch to except: 

    client_id = "1008697610770579556"
    rpc = Presence(client_id)
    rpc.connect()
    rpc.update(
        large_image="ztools",
        large_text="Generating millions of accounts",
        state="Beta v0.1",
        buttons = [{'label':'GitHub',"url":"https://github.com/AndyL0555"}],
        details="Generating millions of accounts.",
        start=int(time.time()),
    )
    #Discord rich presence, client_id depends on user's discord ID. Can be modified easily


    names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
    "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
    "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
    "lydia", "charles", "pedro", "bradley"]
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    print("""
     _____ ______            __    
    /__  //_  __/___  ____  / /____
      / /  / / / __ \/ __ \/ / ___/
     / /__/ / / /_/ / /_/ / (__  )
    /____/_/  \____/\____/_/____/

    """)

    password = input("Enter password: ")
    catchall = input("Enter catchall (Along with @ symbol, e.g. @table.com):")
    postcode = input("Enter postcode: ")
    address1 = input("Enter address (This is for Three Gen): ")
    postcode = input("Enter postcode with space: ")
    def asos():
        link = 'https://my.asos.com/identity/register?lang=en-GB&store=COM&country=GB&keyStoreDataversion=dup0qtf-35&returnUrl=https%3A%2F%2Fwww.asos.com%2Fmen%2F'
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
        #Additions for all these arguments - Selenium is easily detected by many websites due to $cdc in chromedriver.exe. Using HxD Hex editor, I have removed this $cdc hex and replaced
        #it with another value to replace it.
        #Selenium is all based on the chrome tab, meaning that it will be very resource heavy at times when multiple tabs are opened to perform a certain task.
        action = ActionChains(driver)
        fName = random.choice(names)
        lName = random.choice(names)


        nLength = 2
        num = ''.join(random.choice(numbers) for i in range(nLength))
        email = str(fName)+str(lName)+str(num)+catchall
        passw = password

        select1 = Select(driver.find_element(By.XPATH, '//*[@id="BirthDay"]'))
        select2 = Select(driver.find_element(By.XPATH, '//*[@id="BirthMonth"]'))
        select3 = Select(driver.find_element(By.XPATH, '//*[@id="BirthYear"]'))
        file = open("account.txt","a")
        file.write(str(email) + ':' + str(password) + '\n')
        driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(fName)
        driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(lName)
        driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(passw)
        select1.select_by_visible_text('1')
        select2.select_by_visible_text('January')
        select3.select_by_visible_text('2000')
        driver.find_element(By.XPATH, '//*[@id="register"]').click()
        time.sleep(10)
        #Selects values through XPATH and does something, very useful and accurate compared to using CSS selector.

    def three():
        link = 'https://www.three.co.uk/Support/Free_SIM/Order'

        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)
        driver.get(link) #opens link (three)


        fName = random.choice(names)
        lName = random.choice(names)

        nLength = 2
        num = ''.join(random.choice(numbers) for i in range(nLength))
        email = str(fName)+str(lName)+str(num)+catchall #chooses random two numbers and the randomly chosen first and last name, then attaches to catchall


        select = Select(driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select')) #used for selecting value of exact address


        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[1]/span/input').send_keys(fName)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[2]/span/input').send_keys(lName)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[4]/span/input').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[5]/span/input').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[7]/span/input').send_keys(postcode)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/button[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select').click()
        time.sleep(5)
        select.select_by_visible_text(address1)
        elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1400662678121"]/button[2]')))
        elem.click()
        time.sleep(10)

    def main():
        print("1 - Asos gen")
        print("2 - Three sim")
        choice = int(input("Please enter which module you'd like to run: "))
        count = int(input("Enter how many times you'd like to run it: "))
        i = 0
        if choice == 1:
            while i<count:
                asos()
                i+=1
            retry = input("Run bot again? Y/N: ").lower()
            if retry == 'y':
                main()
            else:
                quit()
        elif choice == 2:
            while i<count:
                three()
                i+=1
            retry = input("Run bot again? Y/N: ").lower()
            if retry == 'y':
                main()
            else:
                quit()
        else:
            print("Invalid chocie!")
            main()

    main()
    #Main code, obviously asks user input for what they want to achieve.
API_KEY = 'sk_4077wTzgi7BR880P61gK6SCro5Q87dBA'
#Hyper's authentication API key, user will enter their license key at line 222 and will be pinged as part of the payload. A status code will be returned to determine if the code is real or not. (Through Python requests)
def log(content):
    print('[{}] {}'.format(datetime.utcnow(), content))

def get_license(license_key):
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    req = requests.get(f'https://api.hyper.co/v6/licenses/{license_key}', headers=headers)
    if req.status_code == 200:
        return req.json()

    return None

key = input("Enter license key: ")
license_data = get_license('{}'.format(key))
if license_data:
    if license_data.get('metadata') != {}:
        print('License is already in use on another machine!')
    else:
        print('Authenticated!')
        code()
else:
    print('License not found!')

def update_license(license_key, hardware_id):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'metadata': {
            'hwid': hardware_id
        }
    }

    req = requests.patch(f'https://api.hyper.co/v6/licenses/{license_key}/metadata', headers=headers, json=payload)
    if req.status_code == 200:
        return True

    return None

def reset_license(license_key):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'metadata': {
            'hwid': None
        }
    }

    req = requests.patch(f'https://api.hyper.co/v6/licenses/{license_key}/metadata', headers=headers, json=payload)
    if req.status_code == 200:
        return True
  
    return None
