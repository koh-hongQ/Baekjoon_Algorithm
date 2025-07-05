c=[]
b=0
for i in range(5):
	a=int(input())
	c+=[a]
	b+=a
c.sort()
print(int(b/5))
print(c[2])