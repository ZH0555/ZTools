import random
import time
import os
import re
import uuid
from datetime import datetime

names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
    "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
    "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
    "lydia", "charles", "pedro", "bradley"]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

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

# catchall = input("Enter catchall: ")
# postcode = input("Enter postcode with space: ")
# address = input("Enter address line 1: ")

fName = random.choice(names)
lName = random.choice(names)


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
    driver.get(link) #opens link (three)

    fName = random.choice(names)
    lName = random.choice(names)

    nLength = 2
    num = ''.join(random.choice(numbers) for i in range(nLength))
    email = str(fName)+str(lName)+str(num)+"@"+lines[0] #chooses random two numbers and the randomly chosen first and last name, then attaches to catchall

    aLength = 3
    abc = ''.join(random.choice(letters) for i in range(aLength))
    jigged = str(abc)+ ' ' + str(lines[2])

    tLength = 9
    number = ''.join(random.choice(numbers) for i in range(tLength))
    num = '07'+str(number)
    print(num)

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    print(Fore.GREEN + "Accepting cookie popup...")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/main/div[6]/div[5]/div/div/a').click()
    time.sleep(2)
    print(Fore.GREEN + "Entering email")
    driver.find_element(By.XPATH, '//*[@id="register.email"]').send_keys(email)
    time.sleep(2)
    print(Fore.GREEN + "Entering name")
    driver.find_element(By.XPATH, '//*[@id="register.firstName"]').send_keys(fName)
    time.sleep(2)
    print(Fore.GREEN + "Entering last name")
    driver.find_element(By.XPATH, '//*[@id="register.lastName"]').send_keys(lName)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="checkoutRegisterAddressForm"]/div[5]/div[2]/div[2]/a[2]').click()
    time.sleep(2)
    print(Fore.GREEN + "Entering jigged address")
    driver.find_element(By.XPATH, '//*[@id="addressLine1"]').send_keys(jigged)
    time.sleep(2)
    print(Fore.GREEN + "Entering postcode")
    driver.find_element(By.XPATH, '//*[@id="postCode"]').send_keys(lines[1])
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="city"]').send_keys('London')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="submitOrderBtn"]').click()
    print(Fore.GREEN + "Success!")

count = int(input("How many times would you like the script to run: "))
i = 0
if i<count:
    lebara()
    i+=1
else:
    print("Finished!")
