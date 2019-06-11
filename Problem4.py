#########################################################
import os
import crypt

n=[]
for i in range(0,9):
	n.append(str(i))
username=input('Enter username you want to add :')
password='hello'+username
for i in username:
	if i in n:
		exit('Cannot create user')

#os.system('sudo useradd  '+username)
encpass=crypt.crypt(password,'123')
os.system('sudo useradd -p '+ encpass +' '+username)
 
print("User created")
    
