while True:
	c=input("Enter minimum 500 characters")
	if len(c)>=500:
		break
	else:
		print("Less than 500 character not allowed")

d={}
chars='zyxwvutsrqponmlkjihgfedcba'
print("no of repeted characters")
for i in chars:
	count=c.count(i)
	print(i+" : "+str(count))

print("no of repeted words")
l=c.split(' ')
for i in l:
	count=c.count(i)
	print(i+" : "+str(count))

print("Remove words repeats greater then 5")
l=c.split(' ')
for i in l:
	count=c.count(i)
	d[i]=count
x=list(d.keys())
print(d)
for i in x:
	if d[i] >=5:
		del(d[i])
print(d)
c=""
print("words occurs only one time :")
for i in x:
	if(d[i]==1 and len(c)<500):
		c=c+i

print(c)
	

