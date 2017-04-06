import redis
import tornado
import tornado.web
import tornado.httpserver
from tornado.options import define,options
import redis
import json

define('port',default=8888,type=int)

class DealHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.port=6379
        self.host="localhost"


    def get(self, *args, **kwargs):
        city = self.get_argument("city",None)
        src = self.get_argument("src",None)
        year = self.get_argument("year",None)

        keyset = []
        for i in  range(1,31):
            key = '_'.join([src,city,year,str(i)])
            keyset.append(key)

        r=redis.StrictRedis(host=self.host,port=self.port)
        self.write(r.mget(keyset))

class ExampleHandler(tornado.web.Application):
    def get(self):
        who = self.get_argument('who',None)
        if who:
            self.write("Hello,"+who)
        else:
            self.write("Hello world")

    def post(self):
        who = self.get_argument('who',None)
        if who:
            self.write("Hello,"+who)
        else:
            self.write("Hello world")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",ExampleHandler), #key/value pair http://localhost:8888/ ->ExampleHandler
            (r"deal",DealHandler),
        ]
        settings = []
        tornado.web.Application.__init__(self,handlers,settings)


def creat_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ =="__main__":
    creat_server()