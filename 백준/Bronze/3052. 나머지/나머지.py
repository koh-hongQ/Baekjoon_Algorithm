a=[]
for i in range(10):
	b=int(input())
	a+=[b]

c=[]
for i in a:
	c+= [i%42]
c.sort()


d=set(c)


print(len(d))
