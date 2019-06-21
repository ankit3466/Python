#!/usr/bin/python3
import socket

recv_ip='197.168.43.41'
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

q=0
while q==0:
	a=input("Enter your msg :")
	if len(a)>150:
		print("message should be less then 150 characters")
		a=input("Enter your msg :")
	m=a.encode('ascii')
	s.sendto(m,(recv_ip,recv_port))
	data=s.recvfrom(150)
	ndata=data[0].decode('ascii')
	print(ndata)
	q=int(input("Press 1 for quit the chat and 0 for continue :"))	
