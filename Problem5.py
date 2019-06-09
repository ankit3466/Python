from datetime import datetime

name=input("Enter your name :")
c=datetime.now()

d=c.hour
if(d>=6 and d<12):
    print(name+" Good Morning")
elif(d>=12 and d<18):
    print(name+" Good afternoon")
elif(d>=18 and d<21):
    print(name+" Good evening")
else:
    print(name+" Good night")
