#!/usr/bin/python3


op='''
press 1 to single file view :
press 2 to multiple file view :
press 3 to cat -n view :
press 4 to cat -e view :
'''

print(op)
n=input("Enter your choice")

if(n=='1'):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	print(data)
	f.close()

elif(n=='2'):
	num=int(input('Enter no. of files :'))
	fnames=[]
	print('Enter name of files seperated by enter :')
	for i in range(1,num+1):
		name=input() 
		fnames.append(name)
	
	for i in fnames:
		f=open(i,'r')
		print(f.read())
		f.close()
elif(n== '3'):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	l=1
	for i in a:
		print(str(l)+" "+i)
		l=l+1
		
elif(n=='4'):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	for i in a:
		print(i+"$")
else:
	print("Invalid input...")
	
