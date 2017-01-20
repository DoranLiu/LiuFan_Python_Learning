#!/usr/bin/env python
#coding:utf-8

import paramiko

ssh = paramiko.SSHClient()
# 实例化
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost', 22, 'user', 'pwd')
stdin, stdout, stderr = ssh.exec_command('df')
print (stdout.read())
ssh.close();