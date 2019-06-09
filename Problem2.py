# importing module

from googlesearch import search
import webbrowser

# taking user input
url=input("enter search command")

l=[]

# Storing search url in list l
for i in search(url,stop=10):
        l.append(i)
