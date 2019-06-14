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

	
## create a html code for the images
<html>
<body>
<h1> QRCODE for search hello </h1>
                                                                                                                                                                        
<img src="1.svg"/>
                                                                                                                                                                        
<img src="2.svg"/>
<img src="3.svg"/>
</body>
                                                                                                                                                                        
</html>
                                                                                                                                                                        
## store this code in /var/www/html (you can store images as well in this directory or provides the full path of QR code in img tag )

