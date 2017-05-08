'''
Redis是一个开源（BSD许可），内存数据结构存储，用作数据库，缓存和消息代理。它支持数据结构，例如字符串，散列，列表，集合，具有范围查询的排序集，位图，超文本和具有半径查询的地理空间索引。Redis内置复制，Lua脚本，LRU驱逐，事务和不同级别的磁盘持久性，并通过Redis Sentinel提供高可用性，并通过Redis Cluster进行自动分区。

Redis官网：http : //redis.io/

以上摘自官网介绍
安装的Redis

安装

模块GitHub地址：https：//github.com/WoLpH/redis-py

[root@anshengme ~]# yum -y install redis
配置绑定的IP

[root@anshengme ~]# vim /etc/redis.conf
bind 0.0.0.0
启动并设置开机自启动

[root@anshengme ~]# systemctl start redis
[root@anshengme ~]# systemctl enable redis
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
检查

查看端口

[root@anshengme ~]# netstat -tlnp | grep "redis"
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1439/redis-server 0
数据写入测试

[root@anshengme ~]# /usr/bin/redis-cli
127.0.0.1:6379> set url https://blog.ansheng.me
OK
127.0.0.1:6379> get url
"https://blog.ansheng.me"
127.0.0.1:6379> exit
安装Redis的-PY

安装Redis的-PY

pip3 install redis
或源码安装

python setup.py install
检查安装是否成功

# 导入模块没报错则安装成功
>>> import redis
入门及使用

# 导入模块
>>> import redis
# 连接到Redis服务器
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# 写入一条数据
>>> conn.set('name','ansheng')
True
# 获取一条数据
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
使用连接池连接到Redis的

在幕后，redis-py使用连接池来管理与Redis服务器的连接。默认情况下，您创建的每个Redis实例将依次创建自己的连接池。您可以通过将已创建的连接池实例传递给Redis类的connection_pool参数来覆盖此行为并使用现有的连接池。您可以选择这样做，以实现客户端分片，或者对连接的管理方式进行更细粒度的控制。
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
使用套接字连接

>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
API

redis-py的提供API用来操作redis

String API

set（name，value，ex = None，px = None，nx = False，xx = False）

参数	描述
ex	过期时间（秒）
px	过期时间（毫秒）
nx	如果设置为真，则只有名称不存在时，当前设定操作才执行
xx	如果设置为真，则只有名称存在时，岗前设置操作才执行
>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
setex（名称，值，时间）

设置过期时间/秒

>>> conn.setex('k','v',1)
True
>>> conn.get('k')
psetex（name，time_ms，value）

设置过期时间/毫秒

>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
setnx（name，value）

设置值，只有不存在时，执行设置操作键

>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
mset（* args，** kwargs）

同时设置多个键/值

>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
得到（名称）

获取单个值

>>> conn.get('k1')
b'v1'
mget（keys，* args）

获取多个值

>>> conn.mget('k1','k2')
[b'v1', b'v2']
# 传入列表
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
gotet（名称，值）

设置新值并获取原来的值

>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
getrange（关键，开始，结束）

通过索引的方式来获取值的值

>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
setrange（名称，偏移量，值）

根据索引修改值

>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
setbit（name，offset，value）

getbit（name，offset）

获取值对应某一个索引位置对应的值0/1

>>> conn.getbit('k',1)
1
位数（键，开始=无，结束=无）

获取键对应二进制中表示1的个数

bitop（操作，dest，*键）

将多个值进行值运算，得出的结果保存到一个新值当中

>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
操作支持AND（并），OR（或），NOT（非），XOR（异或）
strlen的（名字）

获取值的长度

>>> conn.set('name','安生')
True
>>> conn.strlen('name')
6
incr（name，amount = 1）

对名称的值进行自增，如果名称不存在则创建，否则自增

>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
incrbyfloat（name，amount = 1.0）

同上，支持浮点数自增

>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
decr（name，amount = 1）

自减，同自增一样，如果进行自减的值不是整数就报错

>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
附加（键值）

在值后面追加内容

>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
哈希API

hset（名称，键值）

设置名称的键值对，有则修改，没有则创建

>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
hmset（名称，映射）

同时设置多个名称的键/值

>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
hget（名称，键）

获取名称中键的值

>>> conn.hget('dic','k2')
b'v2'
hmget（name，keys，* args）

同时获取多个

>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
hgetall（名称）

获取名称对应的所有键/值

>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
为hLen（名称）

获取名称对应键值对的个数

>>> conn.hlen('dic')
2
hkeys（名称）

获取名称中所有的关键

>>> conn.hkeys('dic')
[b'k1', b'k2']
hvals（名称）

获取名称中所有的值

>>> conn.hvals('dic')
[b'v1', b'v2']
六角形（名称，键）

检查当前的名称中是否有传入的关键

>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
hdel（自我，名字，*键）

删除名称中对应的键

>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
hincrby（姓名，密码，金额= 1）

名字中键对应的值进行自增，如果不存在则创建

>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
hincrbyfloat（name，key，amount = 1.0）

值自增，支持浮点数，同上

>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
hscan（name，cursor = 0，match = None，count = None）

增量式迭代获取，HSCAN可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆

参数	描述
name	Redis的的名字
cursor	游标（基于游标分批取获取数据）
match	匹配指定键，默认无表示所有的键
count	每次分片最少获取个数，默认无表示采用的Redis的默认分片个数
hscan_iter（name，match = None，count = None）

利用产量封装HSCAN创建生成器，实现分批去的Redis中获取数据

参数	描述
match	匹配指定键，默认无表示所有的键
count	每次分片最少获取个数，默认无表示采用的Redis的默认分片个数
如：

for item in r.hscan_iter('xx'):
    print item
到期（姓名，时间）

设置过期时间

>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
ListAPI

lpush（name，*值）

在最左边添加值

>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
rpush（name，*值）

在最右边添加值

>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
lpushx（名称，值）

只有名字已经存在时，值添加到列表的最左边

>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
rpushx（名称，值）

只有名字已经存在时，值添加到列表的最右边

>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
LLEN（名称）

获取名称元素的个数

>>> conn.llen('li')
5
linsert（name，where，refvalue，value）

在名称的某一个值前面或者后面插入一个新值

>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
lset（name，index，value）

对名称中的索引索引位置的值进行重新赋值

>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
lrem（name，value，num = 0）

删除指定值后面或者前面的值

NUM = 2，从前到后，删除2个;
NUM = -2，从后向前，删除2个
>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
LPOP（名称）

删除名称中左侧第一个元素

>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
RPOP（名称）

删除名称中右侧第一个元素

>>> conn.rpop('li')
b'33'
lindex（名称，索引）

获取名称中对应索引的值

>>> conn.lindex('li', 0)
b'aa'
lrange（名字，开始，结尾）

使用切片获取数据

>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
ltrim（名称，开始，结尾）

在名称对应的列表中移除没有在开始结束索引之间的值

>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
rpoplpush（src，dst）

从SRC列表中取出最右边的元素，同时将其添加至DST列表的最左边

>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
blpop（keys，timeout = 0）
brpop（keys，timeout = 0）

brpoplpush（src，dst，timeout = 0）

从SRC列表的右侧移除一个元素并将其添加到DST列表的左侧

>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
超时，当时src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0表示永远阻塞
自定义增量迭代

由于redis类库中没有提供对列表元素的增量迭代，如果循环想要name对应的列表的所有元素，那么就需要：

获取名称对应的所有列表
循环列表
但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
使用

for item in list_iter('pp'):
    print item
SET API

sadd（name，* values）

为名称添加值，如果存在则不添加

>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
SCARD（名称）

返回名称的元素数量

>>> conn.scard('s1')
1
sdiff（键，* args）

在按键集合中不在其他集合中的数据

>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
sdiffstore（dest，keys，* args）

在按键集合中不在其他集合中的数据保存到DEST集合中

>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
烧结（键，* args）

获取键集合中与其他集合中的并集

>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
烧结矿（dest，keys，* args）

获取键集合中与其他集合中的并集数据并保存到DEST集合中

>>> conn.sinterstore('news1','s1','s2')
3
sistember（名称，价值）

获取的值是否是名集合中的成员

>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
smembers（名称）

获取名称集合中所有的成员

>>> conn.smembers('news1')
{b'2', b'3', b'1'}
smove（src，dst，value）

将SRC中的值移动到DST中

>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
SPOP（名称）

删除并返回名称中的随机成员

>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
srandmember（姓名，数字=无）

随机获取名称集合中的数个成员，默认编号= 1

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
srem（name，* values）

删除名称集合中的值数据

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
sunion（键，* args）

获取键集合与其他集合的并集

>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
sunionstore（dest，keys，* args）

获取键集合与其他集合的并集并保存到DEST中

>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
有序集API

zadd（name，* args，** kwargs）

>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
zcard（名称）

返回有序集合名称元素的数量

>>> conn.zcard('h1')
2
zcount（name，min，max）

返回在名称中值在最小与最大之间的值个数

>>> conn.zcount('h1',10,30)
2
zincrby（名称，值，金额= 1）

名称中让值的值加上量

>>> conn.zincrby('h1','n1',10)
21.0
zinterstore（dest，keys，aggregate = None）
zlexcount（name，min，max）

zrange（name，start，end，desc = False，withscores = False，score_cast_func = float）

参数	描述
name	Redis的的名字
start	有序集合索引起始位置（非分数）
end	有序集合索引结束位置（非分数）
desc	排序规则，默认按照分数从小到大排序
withscores	是否获取元素的分数，默认只获取元素的值
score_cast_func	对分数进行数据转换的函数
>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
# 从大到小排序
zrevrange(name, start, end, withscores=False, score_cast_func=float)
# 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# 从大到小排序
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
zrangebylex（name，min，max，start = None，num = None）

当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的值（词典排序）来进行排序，而这个命令则可以返回给定的有序集合键中，元素的值介于min和max之间的成员

对于集合中的每个成员进行逐个字节的对比（逐字节比较），并按照从低到高的顺序，返回排序后的集合成员。如果两个字符串有一部分内容是相同的话，那么命令会认为较长的字符串比较短的字符串要大

参数	描述
name	Redis的的名字
min	左区间（值）+表示正无限; - 表示负无限;（表示开区间;
min	右区间（值）
start	对结果进行分片处理，索引位置
num	对结果进行分片处理，索引后面的NUM个元素
如：

ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
更多：

# 从大到小排序
zrevrangebylex(name, max, min, start=None, num=None)
zrevrangebylex（name，max，min，start = None，num = None）

zrangebyscore（name，min，max，start = None，num = None，withscores = False，score_cast_func = float）**

zrank（名称，值）

返回基于0的值，指示在排序集名称的值排名

>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
zrevrank（name，value），从大到小排序
zrem（name，* values）

删除名称中对应的值

>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
zremrangebyrank（name，min，max）

根据排行范围进行删除

>>> conn.zremrangebyrank('h1',1,2)
1
zremrangebyscore（name，min，max）

根据分数范围进行删除

>>> conn.zremrangebyscore('h1',10,20)
2
zscore（名称，值）

返回指定值的值是多少

>>> conn.zscore('h1','n1')
11.0
zunionstore（dest，keys，aggregate = None）

全球API

删除（*名称）

在Redis的中删除名称

>>> conn.delete('ooo')
1
存在（名称）

检测名称是否存在

>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
键（图案= '*'）

# 匹配数据库中所有 key
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
# 匹配hello，hallo和hxllo等
conn.keys(pattern='h?llo')
# 匹配hllo和heeeeello 等
conn.keys(pattern='h*llo')
# 匹配hello和hallo，但不匹配 hillo
conn.keys(pattern='h[ae]llo')
重命名（src，dst）

把SRC重命名成DST

>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
move（name，db）

将Redis的的某个值移动到指定的数据库下

随机key（）

随机获取一个Redis的的名字，不进行删除

>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
类型（名称）

查看名字的类型

>>> conn.type('kk')
b'string'
管道

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，可以则使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline是原子性操作（MySQL中的事务）。

>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# 创建一个通道支持事务
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# 如果在设置上面两个值的过程中出错了，那么这次提交就不会执行
>>> pipe.execute()
[]
发布订阅

# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py 订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py 发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
实例

让Redis的缓存龙卷风页面

# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import time
import redis
poll = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=poll)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        CurrentTim = conn.get('CurrentTim')
        if CurrentTim:
            self.write(CurrentTim)
        else:
            CurrentTim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            conn.set('CurrentTim', CurrentTim, ex=5)
            self.write(CurrentTim)
settings = {
    "tempalte_path": "template",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
数据缓存5秒，如图所示
Redis的-02

基于Redis的的会话存储

app.py

# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import RedisToSession
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = RedisToSession.Session(self)
class MainHandler(BaseHandler):
    def get(self):
        Info = self.session.GetAll()
        self.render("template/index.html", Data=Info)
    def post(self, *args, **kwargs):
        # 获取传过来的值
        Key = self.get_argument('key')
        Val = self.get_argument('val')
        action = self.get_argument('action')
        if action == 'set':
            # 设置值
            self.session[Key] = Val
        elif action == 'del':
            del self.session[Key]
        # 获取所有信息
        Info = self.session.GetAll()
        # 返回给前端渲染
        self.render("template/index.html", Data=Info)
settings = {
    "tempalte_path": "template",
    "cookie_secret": "508CE6152CB93994628D3E99934B83CC",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
模板\ index.html在

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<form action="/" method="post">
    set/del：<input type="text" name="action" value="set"/>
    Key: <input type="text" name="key"/>
    Val: <input type="text" name="val"/>
    <input type="submit" value="设置"/>
</form>
{{ Data }}
</body>
</html>
RedisToSession.py

# _*_ coding: utf-8 _*_
import redis
import hashlib
import uuid
import json
# 连接memcached
pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=pool)
class Session:
    CookieID = 'uc'
    ExpiresTime = 60 * 20
    def __init__(self, handler):
        """
        用于创建用户session在redis中的字典
        :param handler: 请求头
        """
        self.handler = handler
        # 从客户端获取随机字符串
        SessionID = self.handler.get_secure_cookie(Session.CookieID, None)
        # 客户端存在并且在服务端也存在
        if SessionID and conn.exists(SessionID):
            self.SessionID = SessionID
        else:
            # 获取随机字符串
            self.SessionID = self.SessionKey()
            # 把随机字符串写入memcached,时间是20分钟
            conn.hset(self.SessionID, None, None)
        # 每次访问超时时间就加20分钟
        conn.expire(self.SessionID, Session.ExpiresTime)
        # 设置Cookie
        self.handler.set_secure_cookie('uc', self.SessionID)
    def SessionKey(self):
        """
        :return: 生成随机字符串
        """
        UUID = str(uuid.uuid1()).replace('-', '')
        MD5 = hashlib.md5()
        MD5.update(bytes(UUID, encoding='utf-8'))
        SessionKey = MD5.hexdigest()
        return SessionKey
    def __setitem__(self, key, value):
        """
        :param key: session信息中的key
        :param value: 对应的Value
        """
        conn.hset(self.SessionID, key, value)
    def __getitem__(self, item):
        """
        :param item: Session信息中对应的Key
        :return: 获取的Session信息
        """
        # 获取对应的数据
        ResultData = conn.hget(self.SessionID, item)
        return ResultData
    def __delitem__(self, key):
        """
        :param key: 要删除的Key
        """
        conn.hdel(self.SessionID, key)
    def GetAll(self):
        # 获取Session中所有的信息，仅用于测试
        SessionData = conn.hgetall(self.SessionID)
        return SessionData
'''