import paramiko
'''

ssh-keygen -t rsa
ssh-copy-id -i ~/ssh/id_rsa.pub wupeiqi@192.168.159.129
把公钥复制到wupeiqi这台机器

'''

private_key_path = '/home/auto/.ssh/id_rsa' #私钥地址

key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('182.92.219.96 ', 22,username='root' ,pkey=key)

stdin, stdout, stderr = ssh.exec_command('ifconfig')
print (stdout.read())
ssh.close();
