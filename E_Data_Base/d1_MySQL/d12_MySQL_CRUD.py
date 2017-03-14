import pymysql

host = '127.0.0.1'
user = 'root'
passwd = '123456'
db = 'pyMysql'

conn = pymysql.connect(host,user,passwd,db)
cur = conn.cursor()

# 查
# reCount = cur.execute('select * from pyDemo')
# data = cur.fetchall()

#增
# sql = "INSERT INTO pyDemo ( name,age) VALUES(%s,%s)"
# params = ('asd','uio')
# reCount = cur.execute(sql,params)
#
# conn.commit()

#删
# sql = "delete form pyDemo where id = 1"
# reCount = cur.execute(sql)
# conn.commit()


# 改
# sql = "update pyDemo set name = %s where id = 1"
# params = ('tyui')
# reCount = cur.execute(sql,params)
# conn.commit()

#获取字典类型
cur = conn.cursor(cursorclass = pymysql.cursors.DictCursor)
#指针绝对定位
cur.scroll(0,mode='absolute')
#指针相对定位
cur.scroll(-1,mode='relative') #往前一位
#获取自增id值
cur.lastrowid

cur.close()
conn.close()


print(reCount)
# print(data)  # ((1, 'aa', 12), (2, 'vv', 13))
