A=True
while A:
	a=int(input())
	if a==-1:
		A=False
	else:
		c=[]
		for i in range(1,a,1):
			if a%i==0:
				c+=[i]
		p=0
		for i in c:
			p+=i
		if p==a:
			print('%d = ' %a, end='')
			for i in range(0,len(c)-1,1):
				print('%d + ' %(c[i]),end='')
			print(c[len(c)-1])
		else:
			print('%d is NOT perfect.' %a)
