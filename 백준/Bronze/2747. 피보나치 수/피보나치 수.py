a=int(input())

b=1
c=1
i=1
f=2
for i in range(a-1):
	f=b+c
	b=c
	c=f

print(b)