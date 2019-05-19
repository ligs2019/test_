#! /usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
ssh123=paramiko.Transport(('192.168.2.115',22))
ssh123.connect(username='root',password='123456')
sftp=paramiko.SFTPClient.from_transport(ssh123)
sftp.get(r'/opt/yinshu','yinshu999')