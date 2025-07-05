import math
a=int(input())

for k in range(a):
	c=int(input())
	if c==0 or c==1:
		print(2)
	else:
		min=0
		A=True
		while A :
			b=0
			for i in range(2,int(math.sqrt(c))+1,1):
				if c%i==0:
					b+=1
					break
			if b==0 :
				min=c
				A=False
			else:
				c=c+1
		print(min)