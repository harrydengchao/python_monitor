#!/usr/bin/env python
# coding:utf-8
# 网络接口的监测
# netinterface.py

import time
import sys

if len(sys.argv) > 1:
	INTERFACE = sys.argv[1]
else:
	INTERFACE = 'eth0'
STATS = []
print 'Interface: ', INTERFACE

def rx():
	with open('/proc/net/dev', 'rb') as ifstat:
		for interface in ifstat:
			if INTERFACE in interface:
				stat = float(interface.split()[1])
				STATS[0:] = [stat]

def tx():
	with open('/proc/net/dev', 'rb') as ifstat:
		for interface in ifstat:
			if INTERFACE in interface:
				stat = float(interface.split()[9])
				STATS[1:] = [stat]

print "In\t\tOut"

rx()
tx()

while True:
	time.sleep(1)
	rxstat_o = list(STATS)
	rx()
	tx()
	RX = float(STATS[0])
	RX_O = rxstat_o[0]
	TX = float(STATS[1])
	TX_O = rxstat_o[1]
	RX_RATE = round((RX - RX_O)/1024/1024,3)
	TX_RATE = round((TX - TX_O)/1024/1024,3)
	print RX_RATE, "MB",
	print '\t',
	print TX_RATE, "MB"
