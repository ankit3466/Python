#!/usr/bin/python

import socket as s
ip="127.0.0.1"
port=4444

x=s.socket(s.AF_INET,s.SOCK_DGRAM)
x.bind((ip,port))
c=1
while c==1:
	data=x.recvfrom(100)
	print(data[0])
	msg=raw_input("enter your msg :")
	x.sendto(msg,data[1])

	c=input("Press 1 for continue and 0 for end : ")
