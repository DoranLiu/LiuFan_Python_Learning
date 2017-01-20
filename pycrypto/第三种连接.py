import paramiko

scp = paramiko.Transport(('182.92.219.86',22))
scp.connect(username='wupeiqi',password='xxx')
channel = scp.open_session()
print (channel.exec_command('mkdir hello'))
channel.close()
scp.close()