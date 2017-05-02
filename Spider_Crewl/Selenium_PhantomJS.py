from selenium import webdriver

Phantomjs_Path = '/Users/Dery/SeleniumWebDriver/phantomjs-2.1.1-macosx/bin/phantomjs'
# phontomjs 设置代理
dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0")
dcap["phantomjs.page.settings.resourceTimeout"] = ("1000")
service_args = [
    '--proxy=127.0.0.1:1080'
    ] #默认为http代理，可以指定proxy type
driver = webdriver.PhantomJS(executable_path=Phantomjs_Path,service_args=service_args, desired_capabilities=dcap)


import queue
from selenium import webdriver
import threading
import time

class conphantomjs:
	phantomjs_max = 1       #
	jiange = 0.00001        #
	timeout = 20            #
	path="/Users/Dery/SeleniumWebDriver/phantomjs-2.1.1-macosx/bin/phantomjs" # phantomjs 路径
	service_args=['--load-images=no','--disk-cache=yes'] # 不加载图片
	def __init__(self):
		self.q_phantomjs=queue.Queue()   #设置队列
	def getbody(self,url):
		'''

		'''
		d=self.q_phantomjs.get()
		try:
			d.get(url)
		except:
			print ("Phantomjs Open url Error")
		url=d.current_url
		self.q_phantomjs.put(d)
		print (url)

	def open_phantomjs(self):
		'''

		'''
		def open_threading():
			d=webdriver.PhantomJS(conphantomjs.path,service_args=conphantomjs.service_args)
			d.implicitly_wait(conphantomjs.timeout)        ##���ó�ʱʱ��
			d.set_page_load_timeout(conphantomjs.timeout)  ##���ó�ʱʱ��

			self.q_phantomjs.put(d) #��phantomjs���̴������
		th=[]
		for i in range(conphantomjs.phantomjs_max):
			t=threading.Thread(target=open_threading)
			th.append(t)
		for i in th:
			i.start()
			time.sleep(conphantomjs.jiange) #���ÿ�����ʱ����
		for i in th:
			i.join()
	def close_phantomjs(self):
		'''

		'''
		th=[]
		def close_threading():
			d=self.q_phantomjs.get()
			d.quit()
		for i in range(self.q_phantomjs.qsize()):
			t=threading.Thread(target=close_threading)
			th.append(t)
		for i in th:
			i.start()
		for i in th:
			i.join()

if __name__=="__main__":
	'''
    开启phontomJS，并设置并发数
	'''
	cur=conphantomjs()
	conphantomjs.phantomjs_max=2
	cur.open_phantomjs()
	print ("phantomjs num is ",cur.q_phantomjs.qsize())

	url_list=["http://www.baidu.com",'http://www.taobao.com']
	th=[]
	for i in url_list:
		t=threading.Thread(target=cur.getbody,args=(i,))
		th.append(t)
	for i in th:
		i.start()
	for i in th:
		i.join()
	cur.close_phantomjs()

	print ("phantomjs num is ",cur.q_phantomjs.qsize())