import math
a=int(input())
b=int(input())
d=[]
if a==1:
	for j in range(a+1,b+1,1):
		c=0
		for i in range(2,int(math.sqrt(j))+1,1):
			if j%i==0:
				c+=1
				break
		if c!=1:
			d+=[j]
	if len(d)==0:
		print(-1)
	else:
		print(sum(d))
		print(d[0])
else:
	for j in range(a,b+1,1):
		c=0
		for i in range(2,int(math.sqrt(j))+1,1):
			if j%i==0:
				c+=1
				break
		if c!=1:
			d+=[j]
	if len(d)==0:
		print(-1)
	else:
		print(sum(d))
		print(d[0])