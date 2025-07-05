
a=int(input())
b=int(input())

c=[]
for i in range(a,b+1,1):
	for j in range(1,i+1,1):
		if j*j==i:
			c+=[i]
if len(c)==0:
	print(-1)
else:
	print(sum(c))
	print(min(c))