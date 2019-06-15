import smtplib

add=input("Enter your gmail : \n")
passw=input("Enter your pass : \n")
to=input("Enter receiver email : \n")
msg=input("Enter your msg : ")

ms=smtplib.SMTP('smtp.gmail.com',587)
ms.starttls()
ms.login(add,passw)
ms.sendmail(add,to,msg)

print("\n ..sent !!")
ms.quit()
