import redis    #导入redis-py模块

class RedisPool:    #定义了一个连接池类，该类返回连接池中的一个连接给调用者
    def Redis_Pool(self,ClientHost="127.0.0.1",ClientPort=6379,ClientDb=0):
        pool=redis.ConnectionPool(host=ClientHost,port=ClientPort,db=ClientDb)
        return redis.StrictRedis(connection_pool=pool)

class ChangeKey: #该类使用获取到的redis连接对想要进行修改的key进行修改

    def Change_String(self,R,Key,Value):
        try:
            Bool = R.set(Key,Value)
        except Exception as e:
            Bool = False
            print('Insert string Error:',e)
        return Bool

    def Change_List(self,R,KeyName,Key):
        Filed_List=[]
        for i in range(0,len(Key)):
            try:
                R.rpush(KeyName,Key[i])
            except Exception as e:
                Filed_List.append((KeyName,Key[i]))
                print('Insert set Error:',e)
        return Filed_List

    def Change_Hash(self,R,KeyName,Key):
        Filed_List=[]
        for i in Key.keys():
            try:
                R.hset(KeyName,i,Key[i])
            except Exception as e:
                Filed_List.append([i,Key[i]])
                print('Insert set Error:',e)
        return Filed_List

    def Change_Set(self,R,KeyName,Key):
        Filed_List=[]
        NewKey=list(Key)
        for i in range(0,len(NewKey)):
            try:
                R.sadd(KeyName,NewKey[i])
            except Exception as e:
                Filed_List.append(KeyName,NewKey[i])
                print('Insert set Error:',e)
        return Filed_List

    def Change_Key(self,R,Keys):    #通过传递进来的Keys判断其值是属于哪种类型，从而调用不同的key的插入函数将该key插入进redis中
        for i in Keys:
            if isinstance(Keys[i],(str,int,float)):
                print("The key %s type is string,will input new value:" %(i))
                Bool = self.Change_String(R,i,Keys[i])
                if Bool:
                    print("Update is ok,the key:%s New value:%s" %(i,Keys[i]))
                else:
                    print("Update is Filed,the Filed key %s value %s" %(i,Keys[i]))
            elif isinstance(Keys[i],list):
                print("The key %s type is list,will input new value:" %(str(i)))
                Filed_List = self.Change_List(R,i,Keys[i])
                if len(Filed_List) == 0:
                    print("Update is ok,the key:%s New value:%s" %(i,Keys[i]))
                else:
                    print("Update is Filed,the Filed List is %s" %(Filed_List))
            elif isinstance(Keys[i],dict):
                print("The key %s type is hash,will input new value:" %(str(i)))
                Filed_List = self.Change_Hash(R,i,Keys[i])
                if len(Filed_List) == 0:
                    print("Update is ok,the key:%s New value:%s" %(i,Keys[i]))
                else:
                    print("Update is Filed,the Filed List is %s" %(Filed_List))
            elif isinstance(Keys[i],set):
                print("The key %s type is set,will input new value:" %(str(i)))
                Filed_List = self.Change_Set(R,i,Keys[i])
                if len(Filed_List) == 0:
                    print("Update is ok,the key:%s New value:%s" %(i,Keys[i]))
                else:
                    print("Update is Filed,the Filed List is %s" %(Filed_List))
            else:
                print("The Key %s not match that support type.The support type:string,list,hash,set." %(i))
class BatchChangeKey:
    def Batch_Change_Key(self,R,Keys,Value):
        for i in R.keys(Keys):
            self.ChangeKey=ChangeKey()
            self.ChangeKey.Change_Key(R,{i:Value})


def main():
    Pool=RedisPool()    #调用连接池类
    R=Pool.Redis_Pool("127.0.0.1",6379,0)    #获取该连接池中的一个连接
    #keys={'m':'huxianglin','e':[1,2,3],'c':{'z':'a','c':'b'},"abc:def:ghi":set(["a","b","c"])}
      #changekey=ChangeKey()    #使用上面定义的Keys传递给该类，传递的keys要求是一个字典类型的数据
      #changekey.Change_Key(R,keys)
    batchchangekey=BatchChangeKey()    #调用批量修改的类，并将需要批量修改的key的一部分传递进去，可以通过R.keys(key)获取到能匹配的key的list,再遍历这个列表，将value传递进去
    batchchangekey.Batch_Change_Key(R,"abc:defg:*" , "helloworld")

if __name__ == '__main__':
    main()