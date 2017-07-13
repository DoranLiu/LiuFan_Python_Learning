from redis import Redis

r=Redis(host='localhost', port=6379,password=123456)
print(r.keys('*'))
