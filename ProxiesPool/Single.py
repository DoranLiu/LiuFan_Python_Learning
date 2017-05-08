from wsgiref.simple_server import make_server
class ConnectionPool:
    __instance = None
    def __init__(self):
        self.ip = "127.0.0.1"
        # self.port = 3306
        self.pwd = "123456"
        self.username = 'root'
        # 去连接
        self.conn_list = [1,2,3,4,5,6,7,8,9,10]
    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            # 创建一个对象，并将对象赋值给静态字段 __instance
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance
    def get_connection(self):
        # 获取连接
        import random
        r = random.randrange(1,11)
        return r
def index():
    # p = ConnectionPool()
    # print(p)
    p = ConnectionPool.get_instance()
    conn = p.get_connection()
    return "iiiiiii" + str(conn)
def news():
    return 'nnnnnnn'

def RunServer(environ, start_response):
    start_response(status='200 OK', headers=[('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    if url.endswith('index'):
        ret = index()
        return ret
    elif url.endswith('news'):
        ret = news()
        return ret
    else:
        return "404"
if __name__ == '__main__':
    httpd = make_server('', 80, RunServer)
    print("Serving HTTP on port 80...")
    httpd.serve_forever()