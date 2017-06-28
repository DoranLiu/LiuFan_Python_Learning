from selenium import webdriver
import time
import pymysql,random
# # chrome driver 设置代理
# PROXY_IP = "183.131.215.86:8080"
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server={}".format(PROXY_IP))
# driver = webdriver.Chrome(executable_path="/Users/Dery/SeleniumWebDriver/chromedriver",chrome_options=options)
# driver.get("http://www.tianyancha.com")


def get_proxies_ip():
    # MAX_RETRIES = 20
    # session = requests.Session()
    # adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    # session.mount('https://', adapter)
    # session.mount('http://', adapter)
    # rp = session.get(url)
    db = pymysql.connect("localhost", "root", "123456", "Spider_Data", charset='utf8')
    # db = pymysql.connect("192.168.1.231","root","3jw9lketj0","ConstructionMaterials",charset='utf8')
    cursor = db.cursor()
    sql = "SELECT * FROM proxies_info;"
    proxies_list = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            proxy_ip = row[1]
            proxy_port = str(row[2])
            proxies_list.append(proxy_ip + ':' + proxy_port)
    except:
        db.rollback()
    db.close()
    proxies = {
        'http': 'http://' + random.choice(proxies_list)
    }
    return random.choice(proxies_list)

ppp = get_proxies_ip()
print(ppp)
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server={}".format(ppp))
driver = webdriver.Chrome(executable_path="/Users/Dery/SeleniumWebDriver/chromedriver",chrome_options=options)

driver.get("http://www.tianyancha.com")
time.sleep(800)