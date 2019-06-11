###################################################################
#Run in linux

import subprocess

com=input("Enter a command")
f=open('command.txt','a+')
f.seek(0)
data=f.read()

if com in data:
	subprocess.getoutput('echo "command is repeted dont do this" | festival --tts')
else:
	f=open('command.txt','a+')
	f.write(str(com))
	f.write('\n')
	f.close()
	
	if subprocess.getstatusoutput(com)[0] == 0:
		print(subprocess.getoutput(com))
	else:
		subprocess.getoutput('echo "command is incorrect" | festival --tts')
