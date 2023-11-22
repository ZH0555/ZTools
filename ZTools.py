import random
import time
import os
import re
import uuid
from datetime import datetime
import requests

with open("settings.txt") as text:
    lines = []
    for line in text:
        lines.append(line)

try:
    from colorama import Fore, Back, Style
except:
    os.system("pip install colorama")

try:
    import chromedriver_autoinstaller
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
except:
    os.system("pip3 install selenium")

try:
    import undetected_chromedriver as uc
except:
    os.system("pip3 install undetected-chromedriver")

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system("pip install webdriver-manager")

try:
    from pypresence import Presence
except:
    os.system("pip install pypresence")

# Try & Except, only when these libraries have not been installed on user computers will they only branch to except: 

client_id = "1008697610770579556"
rpc = Presence(client_id)
rpc.connect()
rpc.update(
    large_image="ztools",
    large_text="Generating millions of accounts.",
    state="zzzz",
    buttons = [{'label':'Twitter',"url":"https://twitter.com/"}],
    details="zzzz",
    start=int(time.time()),
)


names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def code():
    print("""
    _____ ______            __    
    /__  //_  __/___  ____  / /____
      / /  / / / __ \/ __ \/ / ___/
     / /__/ / / /_/ / /_/ / (__  )
    /____/_/  \____/\____/_/____/
    """)
    fName = random.choice(names)
    lName = random.choice(names)
    
    key = lines[0]
    password = lines[1]
    catchall = lines[2]
    postcode = lines[3]
    address = lines[4]
    city = input("Enter city: ")
    nLength = 2
    num = ''.join(random.choice(numbers) for i in range(nLength))
    email = str(fName)+str(lName)+str(num)+'@'+catchall 

    aLength = 3
    abc = ''.join(random.choice(letters) for i in range(aLength))
    jigged = str(abc)+ ' ' + str(address)

    tLength = 9
    number = ''.join(random.choice(numbers) for i in range(tLength))
    num = '07'+str(number)
    print(num)

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
        #it with another value.
        action = ActionChains(driver)
        fName = random.choice(names)
        lName = random.choice(names)

        select1 = Select(driver.find_element(By.XPATH, '//*[@id="BirthDay"]'))
        select2 = Select(driver.find_element(By.XPATH, '//*[@id="BirthMonth"]'))
        select3 = Select(driver.find_element(By.XPATH, '//*[@id="BirthYear"]'))
        file = open("account.txt","a")
        file.write(str(email) + ':' + str(lines[1]) + '\n')
        driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(fName)
        driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(lName)
        driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(lines[1])
        select1.select_by_visible_text('1')
        select2.select_by_visible_text('January')
        select3.select_by_visible_text('2000')
        driver.find_element(By.XPATH, '//*[@id="register"]').click()
        time.sleep(10)

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
        driver.get(link)


        fName = random.choice(names)
        lName = random.choice(names)

        select = Select(driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select')) #used for selecting value of exact address

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[1]/span/input').send_keys(fName)
        print(Fore.GREEN + "Entering F name.." + "\n")
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[2]/span/input').send_keys(lName)
        print(Fore.GREEN + "Entering L name.." + "\n")
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[4]/span/input').send_keys(email)
        print(Fore.GREEN + "Entering first confirmation email.." + "\n"
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[5]/span/input').send_keys(email)
        print(Fore.GREEN + "Entering confirmation email.." + "\n")
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[7]/span/input').send_keys(postcode)
        print(Fore.GREEN + "Entering postcode.." + "\n")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/button[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select').click()
        time.sleep(5)
        select.select_by_visible_text(address)
        print(Fore.GREEN + "Selecting address.." + "\n")
        elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1400662678121"]/button[2]')))
        elem.click()
        print(Fore.GREEN + "Success" + "\n")
        time.sleep(10)

    def lebara():
        link = 'https://mobile.lebara.com/gb/en/free-sim'
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
        driver.get(link)

        fName = random.choice(names)
        lName = random.choice(names)

        nLength = 2
        num = ''.join(random.choice(numbers) for i in range(nLength))
        email = str(fName)+str(lName)+str(num)+"@"+lines[2]

        aLength = 3
        abc = ''.join(random.choice(letters) for i in range(aLength))
        jigged = str(abc)+ ' ' + str(lines[4])

        tLength = 9
        number = ''.join(random.choice(numbers) for i in range(tLength))
        num = '07'+str(number)

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        print(Fore.GREEN + "Accepting cookie popup..." + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/main/div[6]/div[5]/div/div/a').click()
        time.sleep(2)
        print(Fore.GREEN + "Entering email" + "\n")
        driver.find_element(By.XPATH, '//*[@id="register.email"]').send_keys(email)
        time.sleep(2)
        print(Fore.GREEN + "Entering name" + "\n")
        driver.find_element(By.XPATH, '//*[@id="register.firstName"]').send_keys(fName)
        time.sleep(2)
        print(Fore.GREEN + "Entering last name" + "\n")
        driver.find_element(By.XPATH, '//*[@id="register.lastName"]').send_keys(lName)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="checkoutRegisterAddressForm"]/div[5]/div[2]/div[2]/a[2]').click()
        time.sleep(2)
        print(Fore.GREEN + "Entering address" + "\n")
        driver.find_element(By.XPATH, '//*[@id="addressLine1"]').send_keys(jigged)
        time.sleep(2)
        print(Fore.GREEN + "Entering postcode" + "\n")
        driver.find_element(By.XPATH, '//*[@id="postCode"]').send_keys(lines[3])
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(city)
        print(Fore.GREEN + "Entering city" + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="submitOrderBtn"]').click()
        print(Fore.GREEN + "Success!")

    def main():
        print("1 - Asos gen")
        print("2 - Three sim")
        print("3 - Lebara sim")
        choice = int(input("Please enter which module you'd like to run: "))
        count = int(input("Enter how many times you'd like to run it: "))
        i = 0
        if choice == 1:
            for i in range(1,count+1):
                asos()
                i+=1
            retry = input("Run bot again? Y/N: ").lower()
            if retry == 'y':
                main()
            else:
                quit()
        elif choice == 2:
            for i in range(1,count+1):
                three()
                i+=1
            retry = input("Run bot again? Y/N: ").lower()
            if retry == 'y':
                main()
            else:
                quit()
        elif choice == 3:
            for i in range(1,count+1):
                lebara()
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
API_KEY = 'sk_4077wTzgi7BR880P61gK6SCro5Q87dBA'
#Hyper's authentication API key, user will enter their license key at line 222 and will be sent as part of the payload. Response will be returned to determine the status of the inputted key.
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
key = input("Enter key: ")
license_data = get_license('{}'.format(key)
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
