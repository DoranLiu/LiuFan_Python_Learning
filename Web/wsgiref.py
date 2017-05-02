'''
所有的语言Web框架本质其实就是起一个socket服务端,监听一个端口,然后运行起来
Web框架包含两部分,一部分是socket,另外一部分是业务的逻辑处理,根据请求的不同做不同的处理

Python的Web框架分成了两类：
即包含socket也包含业务逻辑处理的(tornado)
不包含socket(框架本身通过第三方模块实现socket)只包含业务逻辑处理(django,Flask)

WSGI的全称是Web Server Gateway Interface，翻译过来就是Web服务器网关接口。具体的来说，WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来。WSGI一开始是在PEP-0333中定义的，最新版本是在Python的PEP-3333定义的。
'''
'''
下面实例的代码中RunServer()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

environ：一个包含所有HTTP请求信息的dict对象;
start_response：一个发送HTTP响应的函数;
通过wsgiref模块实现一个自定义的web框架

代码的大概逻辑就是: 定义了两个函数index()和manage(),如果用户访问的URL是127.0.0.1:8000/index就返回<h1>/index</h1>,如果用户访问的是127.0.0.1:8000/manage就返回/manage,如果访问其他页面就返回404

无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body,复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
'''
from wsgiref.simple_server import make_server
def index(arg):
    # 返回一个含有html代码的字符串
    return "<h1>%s</h1>" %(arg)
def manage(arg):
    return arg
URLS = {
    "/index": index,
    "/manage": manage,
}
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    if url in URLS.keys():
        func_name = URLS[url]
        ret = func_name(url)
    else:
        ret = "404"
    return ret
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()