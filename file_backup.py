#!/usr/bin/env python
# coding:utf-8
# 文件备份
# file_backup.py

import os
import time

source = ['/home/samba/']
target_dir = '/home/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -qr %s %s' %(target, ''.join(source))

if os.system(zip_command) == 0:
        print 'Successful backup'
else:
        print 'Backup Failed'
