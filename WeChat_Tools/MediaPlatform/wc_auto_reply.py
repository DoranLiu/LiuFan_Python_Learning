import werobot
from werobot.reply import ArticlesReply, Article
from MediaPlatform import send_email
import re

# token填写你的微信 token 值
robot = werobot.WeRoBot(token='liufan',
                        # encoding_aes_key='gagWK7FdAu102lZAfnsBXtFUZU3ux3j1JNB8a6esYZN',
                        # app_id='wxd2c20ef17f90d700'
                        )

# 关注的时候，事件触发此函数
@robot.handler
def welcome(message):
    return "欢迎来到你我的小世界"


# 接收到图片时，触发此函数
@robot.image
def echo(message):

    # 实例化一个图文消息
    reply = ArticlesReply(message=message)

    # 下面的 title, description, img, ulr 就是你要换掉的东西
    article = Article(
        title="Learn By Doing",
        description="实验楼，动手实践学IT",
        img="https://ws1.sinaimg.cn/large/005EFdvdgw1f88zx9nwevj30b4086wev.jpg",
        url="https://github.com/whtsky/WeRoBot"
    )

    # 最多可用 add 10 个，就是平时你见的公众号推送下的其他文章链接
    reply.add_article(article)

    # 返回图文消息
    return reply

# 接收到文字时，触发此函数
@robot.text
def sendEmail(message):

    # 得到用户发送的完整信息
    usermessage = message.content

    #得到用户的邮箱
    email = re.search('\w.*.com',usermessage)

    if email:

        # 得到 eamil 的具体数值
        email = email.group().encode('utf-8')

        #得到用户想发的内容，规定格式为：发邮件到XXXXXX@.com，内容叉叉叉，这个是为了找到 .con 的索引
        index = usermessage.find('com')

        # [index+4:] 其中，index+4代表 'com,' 这四个字符串，也就是说，这四个字符串后面开始算是内容
        content = usermessage[index+4:]

        try:
            # 调用封装好的发邮件函数，传递参数为：发送到的邮箱，发送的内容
            send_email.sendEmail(email,content)
        except:
            return 'False'
        return 'success'
    else:
    # 非发邮件状态下，返回的文字
        return "有种你放学别走！"


robot.run(host='127.0.0.1',port=8000)
