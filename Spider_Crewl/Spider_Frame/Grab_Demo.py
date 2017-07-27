'''
文档 http://docs.grablib.org/en/latest/'''
import logging

from grab import Grab

logging.basicConfig(level=logging.DEBUG)

g = Grab()

g.go('https://github.com/login')
g.doc.set_input('login', '****')
g.doc.set_input('password', '****')
g.doc.submit()

g.doc.save('/tmp/x.html')

g.doc('//ul[@id="user-links"]//button[contains(@class, "signout")]').assert_exists()

home_url = g.doc('//a[contains(@class, "header-nav-link name")]/@href').text()
repo_url = home_url + '?tab=repositories'

g.go(repo_url)

for elem in g.doc.select('//h3[@class="repo-list-name"]/a'):
    print('%s: %s' % (elem.text(),
                      g.make_url_absolute(elem.attr('href'))))