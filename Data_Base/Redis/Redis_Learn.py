'''
Redis是一个开源（BSD许可），内存数据结构存储，用作数据库，缓存和消息代理。
它支持数据结构，例如字符串，散列，列表，集合，具有范围查询的排序集，位图，超文本和具有半径查询的地理空间索引。

Redis内置复制，Lua脚本，LRU驱逐，事务和不同级别的磁盘持久性，并通过Redis Sentinel提供高可用性，并通过Redis Cluster进行自动分区。
'''

# # 连接到Redis服务器
# r = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
# # 写入一条数据
# r.set('name','ansheng')

import redis
import hashlib
import uuid
import json
# 连接memcached
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
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