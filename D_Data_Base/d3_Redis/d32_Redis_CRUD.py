import redis
class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379
        self.write_pool = {}
        self.read_pool=[]
    def wirte(self,website,city,year,month,day,deal_number):

        try:
            key = '_'.join([website,city,str(year),str(month),str(day)])
            val = deal_number
            r = redis.StrictRedis(host=self.host,port=self.port)
            r.set(key,val)
        except Exception as exception:
            print (exception)

    def add_write(self,website,city,year,month,day,deal_number):
        key = '_'.join([website,city,str(year),str(month),str(day)])
        val=deal_number
        self.write_pool[key]=val

    def batch_write(self):
        try:
            r=redis.StrictRedis(host=self.host,port=self.port)
            r.mset(self.write_pool)
        except Exception as exception:
            print (exception)

    def read(self,website,city,year,month,day):
        try:
            key='_'.join([website,city,str(year),str(month),str(day)])
            r=redis.StrictRedis(host=self.host,port=self.port)
            value = r.get(key)
            print (value)
            return value
        except Exception as exception:
            print (exception)

    def add_read(self,website,city,year,month,day):
        key='_'.join(([website,city,str(year),str(month),str(day)]))
        self.read_pool.append(key)

    def batch_read(self):
        try:
            r = redis.StrictRedis(host=self.host,port=self.port)
            val=r.mget(self.read_pool)
        except Exception as exception:
            print (exception)

def single_write(): #单条逐条插入
    db=Database()
    for i in range(1000):
        db.write('meituan','beijing',i,9,1,i)

def batch_write():#一次性插入
    db=Database()
    for i in range(1000):
        db.add_write('meituan','beijing',i,9,1,i)
    db.batch_write()

def single_read():
    db=Database()
    for i in range(1000):
        db.read('meituan','beijing',i,9,1)

def batch_read():
    db=Database()
    for i in range(1000):
        db.batch_read('meituan','beijing',i,9,1)
    db.batch_read()


if __name__ =='__main__':
    db = Database()
    db.wirte('meituan','beijing',2013,8,1,8000)
    db.read('meituan','beijing',2013,8,1)
