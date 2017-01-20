import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='WOshiniba8')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test.py')
t.close()


import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='WOshiniba8')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test.py','/tmp/test2.py')
t.close()