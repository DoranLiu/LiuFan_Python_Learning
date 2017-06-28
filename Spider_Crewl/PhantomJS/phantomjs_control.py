

# import os,re,time,MySQLdb,MySQLdb.cursors,urllib2,random
import requests
import time,os
for i in range(300,400):
    common = '/Users/Dery/SeleniumWebDriver/phantomjs-2.1.1-macosx/bin/phantomjs' + ' phantomjs.js ' + str(i)
    print(time.ctime(),common)
    str_body =  str(os.popen(common).read())
