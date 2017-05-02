'''
使用标准库中的csv模块，可以使用其中reader和writer完成文件读写
'''

import csv

# Read CSV
rf = open('filename.csv', 'rb')
reader = csv.reader(rf)
# 获取的对象是一个可迭代的
reader.next()


# Write CSV
wf = open('filename.csv','wb')
writer = csv.writer(wf)
writer.writerow(['xxx','xxx','xxx','xxx','xxx'])
writer.writerow(reader.next())
wf.flush()

with open('filename.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('new_filename.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)