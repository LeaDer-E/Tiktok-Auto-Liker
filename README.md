# Tiktok Auto Liker
A tool made by "Selenium + Python" that can target specific people to like 150 videos of them on their personal page in no more than five minutes, and you can choose 10 people and leave the tool running to like 1500 videos in approximately 45 minutes only


# Install Command
Open Ur Terminal or CMD then copy & paste:

    pip install selenium
    pip install undetected-chromedriver
    pip install src
    pip install src==0.0.6 
    pip install webdriver_manager
    pip3 install --upgrade requests
   
if ther's some problems at windows Try:

    py -m pip install selenium

# How To Use!
open LeaDer-E.py then put UR E-mail and Password it's the only method right now to login

    username = "E-mail@Address.com"
    password = "Your Pretty Password Here"
    
Then u can Chose The Target Perople you need to give them ur like, and past ther links here:

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
[![Watch the video](https://user-images.githubusercontent.com/99460904/179158938-e161db4b-c111-446a-ab21-0da683a6e8d2.png)](https://www.youtube.com/watch?v=-n0BHvobq0o)
