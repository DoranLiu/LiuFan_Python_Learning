# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def echo():
    print ('hellp world!')

# 格式转成 utf-8
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def sendEmail(email, content):
    # 你的邮箱
    from_addr = 'media_platform@163.com'
    
    # 你的授权码，注意了，大写的注意，不是你邮箱的登录密码，是授权码
    password = 'liufan163mail'
    
    # 你要发送到的邮箱
    # to_addr = email
    to_addr = '695229425@qq.com'

    # 163 的 smtp 服务器
    smtp_server = 'smtp.163.com'
    
    # 发送邮件的内容
    msg = MIMEText(content, 'plain', 'utf-8')
    
    # 发邮件的人的邮箱
    msg['From'] = _format_addr(u'Ur Lover <%s>' % from_addr)
    
    # 要发送到的邮箱
    msg['To'] = _format_addr(u'My Lover <%s>' % to_addr)
    
    # 发送的邮件标题
    msg['Subject'] = Header(u'Prediction', 'utf-8').encode()
    
    # 连接服务器，163的smtp端口号，为25
    server = smtplib.SMTP(smtp_server, 25)
    
    # set_debuglevel大于0时将启用调试模式，也就是输出链接信息，发送头信息等。
    server.set_debuglevel(1)
    
    # 登录邮箱
    server.login(from_addr, password)
    
    # 发送邮件
    server.sendmail(from_addr, [to_addr], msg.as_string())
    
    # 退出服务器
    server.quit()