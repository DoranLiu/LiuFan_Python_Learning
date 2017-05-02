'在Web应用中常用JSON（JavaScript Object Notation）格式传输数据'

import json
# 创建一个列表
l = [1,2,'asd',{'blgo_url','ansheng.me'}]
# 使用dumps转换为字符串
json.dumps(l)
'[1, 2, "asd", {"blgo_url": "ansheng.me"}]'
# 去掉空格
json.dumps(l, separators=[',',':'])
'[1,2,"asd",{"blgo_url":"ansheng.me"}]'
# 排序
d = {'b':None,'a':'111','g':'Null'}
json.dumps(d, sort_keys=True)
'{"a": "111", "b": null, "g": "Null"}'
# 将字符串转换为数据类型
json.loads('[1,2,"asd",{"blgo_url":"ansheng.me"}]')
"[1, 2, 'asd', {'blgo_url': 'ansheng.me'}]"