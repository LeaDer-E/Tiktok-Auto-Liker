#login Information
username = "Ur E-mail"
password = "UrPassword"

######################################################################################################################
#Links
Per1 = ('Person1')
Per2 = ('Person2')
Per3 = ('Person3')
Per4 = ('Person4')
Per5 = ('Person5')
Per6 = ('Person6')
Per7 = ('Person7')
Per8 = ('Person8')
Per9 = ('Person9')
Per10 = ('Person10')

######################################################################################################################

print('#I hope you like this tool, and it be useful for you to use it, and you can support me at: "www.buymeacoffee.com/LeaDer.E"')
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import *
#from selenium.webdriver import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.relative_locator import locate_with
import time
import logging
import os
import time
import random
import time
import undetected_chromedriver.v2 as uc
import undetected_chromedriver as uc
import os
from pathlib import Path
options = Options()

######################################################################################################################

#Browser Choosen
browser_name = "undetectable"
if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #options.add_argument("user-data-dir=/home/eslammustafa/.config/google-chrome/Default")
    options.headless = True
    driver = webdriver.Chrome(executable_path="/home/leader/Desktop/Python Workstation/Tiktok Follower/chromedriver", chrome_options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path="/home/eslammustafa/Desktop/PY Projects/geckodriver")
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options= options)

elif browser_name == "undetectable":
    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(use_subprocess=True,
    options=chrome_options,
    seleniumwire_options={}
    )
    #driver = uc.Chrome()
    #options = uc.ChromeOptions()

elif browser_name == 'stealth':
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=r"/home/eslammustafa/Desktop/PY Projects/chromedriver")
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

else:
    print ("Please pass the correct browser name: " + browser_name)

action = ActionChains(driver)
######################################################################################################################
#Likes
def Likes():
    s1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]').click()
    Scroll = driver.find_element(By.CSS_SELECTOR, "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-7t2h2f-DivBrowserModeContainer.e11s2kul0 > div.tiktok-5uccoo-DivVideoContainer.e11s2kul27 > button.tiktok-2xqv0y-ButtonBasicButtonContainer-StyledVideoSwitchV2.e11s2kul15 > svg")
    
    Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
    action.double_click(Like).perform()
    #Like No.(1)
    try:
        Scroll.click()
        print('(1)[♥] Like Done [>.-]')
    except:
        print('(1)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(2)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(2)[♥] Like Done [>.-]')
    except:
        print('(2)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(3)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(3)[♥] Like Done [>.-]')
    except:
        print('(3)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(4)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(4)[♥] Like Done [>.-]')
    except:
        print('(4)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(5)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(5)[♥] Like Done [>.-]')
    except:
        print('(5)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(6)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(6)[♥] Like Done [>.-]')
    except:
        print('(6)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(7)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(7)[♥] Like Done [>.-]')
    except:
        print('(7)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(8)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(8)[♥] Like Done [>.-]')
    except:
        print('(8)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(9)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(9)[♥] Like Done [>.-]')
    except:
        print('(9)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(10)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(10)[♥] Like Done [>.-]')
    except:
        print('(10)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(11)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(11)[♥] Like Done [>.-]')
    except:
        print('(11)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(12)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(12)[♥] Like Done [>.-]')
    except:
        print('(12)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(13)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(13)[♥] Like Done [>.-]')
    except:
        print('(13)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(14)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(14)[♥] Like Done [>.-]')
    except:
        print('(14)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(15)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(15)[♥] Like Done [>.-]')
    except:
        print('(15)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(16)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(16)[♥] Like Done [>.-]')
    except:
        print('(16)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(17)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(17)[♥] Like Done [>.-]')
    except:
        print('(17)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(18)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(18)[♥] Like Done [>.-]')
    except:
        print('(18)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(19)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(19)[♥] Like Done [>.-]')
    except:
        print('(19)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(20)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(20)[♥] Like Done [>.-]')
    except:
        print('(20)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(21)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(21)[♥] Like Done [>.-]')
    except:
        print('(21)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(22)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(22)[♥] Like Done [>.-]')
    except:
        print('(22)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(23)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(23)[♥] Like Done [>.-]')
    except:
        print('(23)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(24)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(24)[♥] Like Done [>.-]')
    except:
        print('(24)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(25)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(25)[♥] Like Done [>.-]')
    except:
        print('(25)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(26)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(26)[♥] Like Done [>.-]')
    except:
        print('(26)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(27)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(27)[♥] Like Done [>.-]')
    except:
        print('(27)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(28)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(28)[♥] Like Done [>.-]')
    except:
        print('(28)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(29)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(29)[♥] Like Done [>.-]')
    except:
        print('(29)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(30)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(30)[♥] Like Done [>.-]')
    except:
        print('(30)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(31)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(31)[♥] Like Done [>.-]')
    except:
        print('(31)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(32)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(32)[♥] Like Done [>.-]')
    except:
        print('(32)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(33)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(33)[♥] Like Done [>.-]')
    except:
        print('(33)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(34)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(34)[♥] Like Done [>.-]')
    except:
        print('(34)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(35)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(35)[♥] Like Done [>.-]')
    except:
        print('(35)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(36)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(36)[♥] Like Done [>.-]')
    except:
        print('(36)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(37)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(37)[♥] Like Done [>.-]')
    except:
        print('(37)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(38)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(38)[♥] Like Done [>.-]')
    except:
        print('(38)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(39)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(39)[♥] Like Done [>.-]')
    except:
        print('(39)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(40)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(40)[♥] Like Done [>.-]')
    except:
        print('(40)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(41)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(41)[♥] Like Done [>.-]')
    except:
        print('(41)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(42)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(42)[♥] Like Done [>.-]')
    except:
        print('(42)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(43)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(43)[♥] Like Done [>.-]')
    except:
        print('(43)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(44)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(44)[♥] Like Done [>.-]')
    except:
        print('(44)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(45)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(45)[♥] Like Done [>.-]')
    except:
        print('(45)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(46)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(46)[♥] Like Done [>.-]')
    except:
        print('(46)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(47)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(47)[♥] Like Done [>.-]')
    except:
        print('(47)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(48)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(48)[♥] Like Done [>.-]')
    except:
        print('(48)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(49)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(49)[♥] Like Done [>.-]')
    except:
        print('(49)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(50)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(50)[♥] Like Done [>.-]')
    except:
        print('(50)[+] Maybe Done Here, Please wait a Minute')

    print('Breaking')    
    time.sleep(60)

    #Like No.(51)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(51)[♥] Like Done [>.-]')
    except:
        print('(51)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(52)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(52)[♥] Like Done [>.-]')
    except:
        print('(52)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(53)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(53)[♥] Like Done [>.-]')
    except:
        print('(53)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(54)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(54)[♥] Like Done [>.-]')
    except:
        print('(54)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(55)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(55)[♥] Like Done [>.-]')
    except:
        print('(55)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(56)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(56)[♥] Like Done [>.-]')
    except:
        print('(56)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(57)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(57)[♥] Like Done [>.-]')
    except:
        print('(57)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(58)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(58)[♥] Like Done [>.-]')
    except:
        print('(58)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(59)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(59)[♥] Like Done [>.-]')
    except:
        print('(59)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(60)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(60)[♥] Like Done [>.-]')
    except:
        print('(60)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(61)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(61)[♥] Like Done [>.-]')
    except:
        print('(61)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(62)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(62)[♥] Like Done [>.-]')
    except:
        print('(62)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(63)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(63)[♥] Like Done [>.-]')
    except:
        print('(63)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(64)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(64)[♥] Like Done [>.-]')
    except:
        print('(64)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(65)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(65)[♥] Like Done [>.-]')
    except:
        print('(65)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(66)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(66)[♥] Like Done [>.-]')
    except:
        print('(66)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(67)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(67)[♥] Like Done [>.-]')
    except:
        print('(67)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(68)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(68)[♥] Like Done [>.-]')
    except:
        print('(68)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(69)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(69)[♥] Like Done [>.-]')
    except:
        print('(69)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(70)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(70)[♥] Like Done [>.-]')
    except:
        print('(70)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(71)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(71)[♥] Like Done [>.-]')
    except:
        print('(71)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(72)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(72)[♥] Like Done [>.-]')
    except:
        print('(72)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(73)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(73)[♥] Like Done [>.-]')
    except:
        print('(73)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(74)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(74)[♥] Like Done [>.-]')
    except:
        print('(74)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(75)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(75)[♥] Like Done [>.-]')
    except:
        print('(75)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(76)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(76)[♥] Like Done [>.-]')
    except:
        print('(76)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(77)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(77)[♥] Like Done [>.-]')
    except:
        print('(77)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(78)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(78)[♥] Like Done [>.-]')
    except:
        print('(78)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(79)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(79)[♥] Like Done [>.-]')
    except:
        print('(79)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(80)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(80)[♥] Like Done [>.-]')
    except:
        print('(80)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(81)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(81)[♥] Like Done [>.-]')
    except:
        print('(81)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(82)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(82)[♥] Like Done [>.-]')
    except:
        print('(82)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(83)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(83)[♥] Like Done [>.-]')
    except:
        print('(83)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(84)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(84)[♥] Like Done [>.-]')
    except:
        print('(84)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(85)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(85)[♥] Like Done [>.-]')
    except:
        print('(85)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(86)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(86)[♥] Like Done [>.-]')
    except:
        print('(86)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(87)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(87)[♥] Like Done [>.-]')
    except:
        print('(87)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(88)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(88)[♥] Like Done [>.-]')
    except:
        print('(88)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(89)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(89)[♥] Like Done [>.-]')
    except:
        print('(89)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(90)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(90)[♥] Like Done [>.-]')
    except:
        print('(90)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(91)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(91)[♥] Like Done [>.-]')
    except:
        print('(91)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(92)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(92)[♥] Like Done [>.-]')
    except:
        print('(92)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(93)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(93)[♥] Like Done [>.-]')
    except:
        print('(93)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(94)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(94)[♥] Like Done [>.-]')
    except:
        print('(94)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(95)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(95)[♥] Like Done [>.-]')
    except:
        print('(95)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(96)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(96)[♥] Like Done [>.-]')
    except:
        print('(96)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(97)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(97)[♥] Like Done [>.-]')
    except:
        print('(97)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(98)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(98)[♥] Like Done [>.-]')
    except:
        print('(98)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(99)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(99)[♥] Like Done [>.-]')
    except:
        print('(99)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(100)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(100)[♥] Like Done [>.-]')
    except:
        print('(100)[+] Maybe Done Here, Please wait a Minute')
    
    print('Breaking')    
    time.sleep(60)

    #Like No.(101)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(101)[♥] Like Done [>.-]')
    except:
        print('(101)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(102)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(102)[♥] Like Done [>.-]')
    except:
        print('(102)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(103)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(103)[♥] Like Done [>.-]')
    except:
        print('(103)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(104)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(104)[♥] Like Done [>.-]')
    except:
        print('(104)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(105)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(105)[♥] Like Done [>.-]')
    except:
        print('(105)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(106)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(106)[♥] Like Done [>.-]')
    except:
        print('(106)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(107)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(107)[♥] Like Done [>.-]')
    except:
        print('(107)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(108)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(108)[♥] Like Done [>.-]')
    except:
        print('(108)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(109)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(109)[♥] Like Done [>.-]')
    except:
        print('(109)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(110)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(110)[♥] Like Done [>.-]')
    except:
        print('(110)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(111)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(111)[♥] Like Done [>.-]')
    except:
        print('(111)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(112)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(112)[♥] Like Done [>.-]')
    except:
        print('(112)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(113)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(113)[♥] Like Done [>.-]')
    except:
        print('(113)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(114)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(114)[♥] Like Done [>.-]')
    except:
        print('(114)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(115)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(115)[♥] Like Done [>.-]')
    except:
        print('(115)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(116)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(116)[♥] Like Done [>.-]')
    except:
        print('(116)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(117)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(117)[♥] Like Done [>.-]')
    except:
        print('(117)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(118)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(118)[♥] Like Done [>.-]')
    except:
        print('(118)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(119)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(119)[♥] Like Done [>.-]')
    except:
        print('(119)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(120)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(120)[♥] Like Done [>.-]')
    except:
        print('(120)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(121)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(121)[♥] Like Done [>.-]')
    except:
        print('(121)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(122)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(122)[♥] Like Done [>.-]')
    except:
        print('(122)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(123)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(123)[♥] Like Done [>.-]')
    except:
        print('(123)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(124)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(124)[♥] Like Done [>.-]')
    except:
        print('(124)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(125)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(125)[♥] Like Done [>.-]')
    except:
        print('(125)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(126)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(126)[♥] Like Done [>.-]')
    except:
        print('(126)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(127)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(127)[♥] Like Done [>.-]')
    except:
        print('(127)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(128)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(128)[♥] Like Done [>.-]')
    except:
        print('(128)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(129)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(129)[♥] Like Done [>.-]')
    except:
        print('(129)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(130)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(130)[♥] Like Done [>.-]')
    except:
        print('(130)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(131)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(131)[♥] Like Done [>.-]')
    except:
        print('(131)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(132)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(132)[♥] Like Done [>.-]')
    except:
        print('(132)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(133)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(133)[♥] Like Done [>.-]')
    except:
        print('(133)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(134)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(134)[♥] Like Done [>.-]')
    except:
        print('(134)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(135)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(135)[♥] Like Done [>.-]')
    except:
        print('(135)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(136)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(136)[♥] Like Done [>.-]')
    except:
        print('(136)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(137)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(137)[♥] Like Done [>.-]')
    except:
        print('(137)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(138)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(138)[♥] Like Done [>.-]')
    except:
        print('(138)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(139)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(139)[♥] Like Done [>.-]')
    except:
        print('(139)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(140)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(140)[♥] Like Done [>.-]')
    except:
        print('(140)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(141)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(141)[♥] Like Done [>.-]')
    except:
        print('(141)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(142)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(142)[♥] Like Done [>.-]')
    except:
        print('(142)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(143)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(143)[♥] Like Done [>.-]')
    except:
        print('(143)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(144)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(144)[♥] Like Done [>.-]')
    except:
        print('(144)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(145)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(145)[♥] Like Done [>.-]')
    except:
        print('(145)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(146)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(146)[♥] Like Done [>.-]')
    except:
        print('(146)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(147)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(147)[♥] Like Done [>.-]')
    except:
        print('(147)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(148)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(148)[♥] Like Done [>.-]')
    except:
        print('(148)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(149)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(149)[♥] Like Done [>.-]')
    except:
        print('(149)[+] Maybe Done Here, Please wait a Minute')

    #Like No.(150)
    try:
        Scroll.click()
        Like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[1]/div')
        action.double_click(Like).perform()
        print('(150)[♥] Like Done [>.-]')
    except:
        print('(150)[+] Maybe Done Here, Please wait a Minute')
    
    print('Breaking')    
    time.sleep(60)
    

######################################################################################################################

#Login
url1 = ('https://www.tiktok.com/login/phone-or-email/email')
driver.get(url1)
time.sleep(2)
print('login process...')
password1 = driver.find_element(By.CSS_SELECTOR, '#loginContainer > div.tiktok-xabtqf-DivLoginContainer.exd0a430 > form > div.tiktok-15iauzg-DivContainer.ewblsjs0 > div > input')
password1.send_keys(password)
print('password done')
username1 = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[3]/input')
username1.send_keys(username)
print('email done')
print('Login Succsessfull')
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/form/button").click()
time.sleep(30)

######################################################################################################################

#startup
driver.get(Per1)
print ("Going to Person No.: [1]..")
time.sleep(5)
Likes()

driver.get(Per2)
print ("Going to Person No.: [2]..")
time.sleep(5)
Likes()

driver.get(Per3)
print ("Going to Person No.: [3]..")
time.sleep(5)
Likes()

driver.get(Per4)
print ("Going to Person No.: [4]..")
time.sleep(5)
Likes()

driver.get(Per5)
print ("Going to Person No.: [5]..")
time.sleep(5)
Likes()

driver.get(Per6)
print ("Going to Person No.: [6]..")
time.sleep(5)
Likes()

driver.get(Per7)
print ("Going to Person No.: [7]..")
time.sleep(5)
Likes()

driver.get(Per8)
print ("Going to Person No.: [8]..")
time.sleep(5)
Likes()

driver.get(Per9)
print ("Going to Person No.: [9]..")
time.sleep(5)
Likes()

driver.get(Per10)
print ("Going to Person No.: [10]..")
time.sleep(5)
Likes()


