#!/usr/bin/python3
import socket

recv_ip='197.168.43.41'
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

q=0
while q==0:
	data=s.recvfrom(150)
	ndata=data[0].decode('ascii')
	print("From Sender :",ndata )
	rpl=input("Your reply : ")
	if len(rpl)>150:
		print("reply should be less then 150 characters")
		rpl=input("Your reply :")
	send=rpl.encode('ascii')
	s.sendto(send,data[1])
	q=int(input("Press 1 to quit the chat and 0 for continue :"))
