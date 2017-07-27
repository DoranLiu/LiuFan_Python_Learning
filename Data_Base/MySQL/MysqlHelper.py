import pymysql

class MySQLHelper():
    def __init__(self,host,db_name,user,passwd,charset='utf8',port=3306):
        self.host = host
        self.port = port
        self.db = db_name
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.user,oasswd=self.passwd,charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def curd(self,sql,params):
        try:
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()

            self.close()
        except Exception as e:
            print(e)

    def select_all(self,sql,params):
        try:
            self.open()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)

