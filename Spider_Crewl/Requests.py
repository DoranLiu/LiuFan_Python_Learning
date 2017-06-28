import requests,re,random,pymysql
from bs4 import BeautifulSoup
from multiprocessing import Pool,Lock
import http.cookiejar


# 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
headers= {
          }
login_data = {
    }
login_url = ''

session = requests.Session()
filename = 'cookie'
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# 而MozillaCookieJar类是存为'/.txt'格式的文件
session.cookies = http.cookiejar.LWPCookieJar(filename)
# 若本地有cookie则不用再post数据了
try:
    session.cookies.load(filename=filename, ignore_discard=True)
except:
    print('未加载Cookie')
content = session.post(login_url,data=login_data,headers=headers)
print(content.content)
# 保存cookie到本地
session.cookies.save(ignore_discard=True, ignore_expires=True)

url = 'http://www.tianyancha.com/v2/company/437099469.json'
req = session.get(url,allow_redirects=False,headers=headers,timeout=60)
print(req.text)