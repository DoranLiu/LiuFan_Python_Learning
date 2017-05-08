'''
Paramiko是一个Python实施SSHv2的协议，提供客户端和服务器的功能。虽然它利用一个Python C扩展低级别加密的paramiko本身就是围绕SSH联网概念的纯Python接口。
Paramiko官网：http://www.paramiko.org/
'''

# 安装Paramiko
# pip3 install paramiko
# 安装之后进入python解释器导入模块，如果导入成功则安装成功，否则安装失败.
import paramiko
# 使用用户名与密码的方式连接

# 导入paramiko模块
import paramiko
# 创建SSHClient对象
ssh = paramiko.SSHClient()
# 如果是一个新主机连接，会出现yes/no，AutoAddPolicy自动填写yes的
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.56.100', port=22, username='root', password='123456')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -h')
# 获取正确的输出
result = stdout.read()
# 关闭连接
ssh.close()
# 获取到的值
result
b'Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda3        48G  3.3G   45G   7% /\ndevtmpfs        984M     0  984M   0% /dev\ntmpfs           993M     0  993M   0% /dev/shm\ntmpfs           993M  8.9M  984M   1% /run\ntmpfs           993M     0  993M   0% /sys/fs/cgroup\n/dev/sda1       197M  137M   60M  70% /boot\ntmpfs           199M     0  199M   0% /run/user/0\n'

# 使用密钥的方式连接
# 在使用密钥的方面连接之前我们需要先做ssh-key认证，步骤如下：
# [root@linux-node1 ~]# ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
# 然后下载/root/.ssh/id_rsa下载下来，复制到E:\python-intensive-training\目录系，下面是在windows下使用paramiko连接脚本如下

# 指定密钥的文件
private_key = paramiko.RSAKey.from_private_key_file('E:\python-intensive-training\id_rsa')
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机，要不然一台新机器去连接它的时候会让你输入yes/no
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.56.100', port=22, username='root', pkey=private_key)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -h')
"""
stdin：标准输入
stdout：标准输出
stderr：错误输出
"""
# 获取命令执行的正确结果
result = stdout.read()
# 关闭连接
ssh.close()
# 输出执行结果
print(str(result, encoding='utf-8'))

'''# 文件上传与下载'''
t = paramiko.Transport(('192.168.56.100', 22))
t.connect(username="root", password="123456")
sftp = paramiko.SFTPClient.from_transport(t)
# 远程目录
remotepath = '/tmp/id_rsa'
# 本地文件
localpath = 'id_rsa'
# 上传文件
sftp.put(localpath, remotepath)
# 下载文件
# sftp.get(remotepath, localpath)
# 关闭连接
t.close()