a,b=map(int, input().split())

c=[]
if a<b:
	c+=[a] #요게 겁나 중요. 그냥 바로 print(a)가 아니였음.
	
	p=[]
	p1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	p[:]=p1
	for i in range(len(c)):
		if 10<=c[i]<=35:
			c[i]=p[c[i]-10]

	for i in range(len(c)):
		print(c[len(c)-1-i],end='')
else:

	A=True
	while A:
		c+=[a%b] 
		a=a//b
		if a<b:
			c+=[a]
			A=False


	p=[]
	p1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	p[:]=p1
	for i in range(len(c)):
		if 10<=c[i]<=35:
			c[i]=p[c[i]-10]

	for i in range(len(c)):
		print(c[len(c)-1-i],end='')