# Tiktok Commenter Follow
A tool made by "Selenium + Python" that can target specific people to like 150 videos of them on their personal page in no more than five minutes, and you can choose 10 people and leave the tool running to like 1500 videos in approximately 45 minutes only


# Install Command
Open Ur Terminal or CMD then copy & paste:

    pip install selenium
    pip install undetected-chromedriver
    pip install src
    pip install src==0.0.6 
    pip install webdriver_manager
    pip3 install --upgrade requests

# How To Use!
open LeaDer-E.py then put UR E-mail and Password it's the only method right now to login

    username = "E-mail@Address.com"
    password = "Your Pretty Password Here"
    
Then u can Chose The Target Vedios you need, but u have choose the vedios that have more than 100 comment and past ther links here:

    ######################################################################################################################
    #Links
    Per1 = ('https://www.tiktok.com/@momabdoahmed')
    Per2 = ('https://www.tiktok.com/@_n.b8_8')
    Per3 = ('https://www.tiktok.com/@user60010882611541')
    Per4 = ('https://www.tiktok.com/@user472060960anzr')
    Per5 = ('https://www.tiktok.com/@dyl70sv1mm7z')
    Per6 = ('tiktok.com/@nadanas7er')
    Per7 = ('https://www.tiktok.com/@maryoma595')
    Per8 = ('https://www.tiktok.com/@user3529676852721')
    Per9 = ('https://www.tiktok.com/@gtxgtg')
    Per10 = ('https://www.tiktok.com/@momabdoahmed')
    ######################################################################################################################

## Speed 
the code make 150 Likes at every 2 min. but i have but sleep time 1 min. every 50 likes, it's can like 150 vedio every 5 min, i think it's good, to don't get ban from Likes for one day.

## Browser 
you have to choose your best automation browser, but i'am like the "undetectable browser because it's the best at this tool

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

## Known Issues

Any issues are usually because the underlying browser automation framework has a
bug or inconsistency. Where possible, we try to cover up these underlying
problems in the client, but sometimes workarounds require higher-level
intervention.
try to restart the code or change the vedio link
Please feel free to file an [issue][issue] if this client doesn't work as
expected.

[issue]: https://github.com/LeaDer-E/Tiktok-Auto-Liker/issues/new

# Vedio on youtube
Soon


# Support
<a href="https://www.buymeacoffee.com/LeaDer.E" target="_blank" rel="noopener noreferrer"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
