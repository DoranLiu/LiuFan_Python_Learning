from selenium import webdriver

# chrome driver 设置代理
PROXY_IP = "<some IP address>"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server={}".format(PROXY_IP))
driver = webdriver.Chrome(executable_path="/Users/Dery/SeleniumWebDriver/chromedriver",chrome_options=options)
driver.get("<site URL>")