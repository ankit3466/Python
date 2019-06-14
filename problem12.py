import pyqrcode
from googlesearch import search

n=input("Enter your search :")
url=[]
j=1
for i in search(n,stop=3):
	url.append(i)
	qr=pyqrcode.create(i)
	qr.svg(str(j)+".svg",scale=8)
	j=j+1

