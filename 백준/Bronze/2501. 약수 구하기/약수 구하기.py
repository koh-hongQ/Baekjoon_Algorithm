c=[]
a,b=map(int,input().split())
for i in range(1,a+1,1):
	if a%i==0:
		c+=[i]

if b>len(c):
	print(0)
else:
	print(c[b-1])