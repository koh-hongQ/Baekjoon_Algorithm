a=[]
for i in range (9):
	b= int(input())
	a+=[b]
	
	
c=0
for i in a:
	if i>c:
		c=i

print(c, a.index(c)+1)