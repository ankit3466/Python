# importing library
import smtplib

# taking input from user about sender email and password also receiver address
add=input("Enter your gmail : \n")
passw=input("Enter your pass : \n")
to=input("Enter receiver email : \n")
msg=input("Enter your msg : ")

# setting smtp protocol
ms=smtplib.SMTP('smtp.gmail.com',587)
ms.starttls()

# login into sender account
ms.login(add,passw)
# sending mail to receiver
ms.sendmail(add,to,msg)

print("\n ..sent !!")

# logout from the server and quit the connection
ms.quit()
