op='''
press 1 for create single file :
press 2 for multiple file creation :
press 3 for touch -c command :
'''
print(op)
c=input("Enter your choice")

if(c=='1'):
	fname=input("enter file name : ")	
	f=open(fname,'w')
	f.close()
	print("File created")
elif(c=='2'):
	n=int(input("how many file you want to create : "))
	l=[]
	for i in range(n):
		l.append(input("enter file name : "))
	for i in l:
		f=open(i,'w')
		f.close()
	print("File created")

elif(c=='3'):
	a=input("enter file name : ")
	print("command run successfully")
	exit()
else:
	print("Invalid Input...")
