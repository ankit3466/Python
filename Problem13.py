import pyttsx3
import datetime as dt
import os

s=pyttsx3.init()
s.say("Hey, Ankit Gupta")
s.runAndWait()

d=dt.datetime.now().hour
if(d>=6 and d<12):
        s.say(" Good Morning")
elif(d>=12 and d<18):
        s.say(" Good afternoon")
elif(d>=18 and d<21):
	s.say(" Good evening")
else:
	s.say(" Good night")
s.runAndWait()
s.stop()
def add(*a):
	sums=0
	for i in a:
		sums=sums+i
	print(sums)


def sort(*v):
	print(sorted(v))

	
def inst_mod():
        help('modules')
	x=os.system('pip3 list | wc -l')
	print(x)
