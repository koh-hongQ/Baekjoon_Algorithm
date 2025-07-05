A=True
while A:
	d=[]
	a,b,c=map(int,input().split())
	d+=[a]
	d+=[b]
	d+=[c]
	d.sort()
	a=d[0]
	b=d[1]
	c=d[2]
	if a+b>c:
		if a==b==c!=0:
			print('Equilateral')
		elif  a==b and b!=c:
			print('Isosceles')
		elif  c==b and a!=c:
			print('Isosceles')
		elif  a==c and b!=a:
			print('Isosceles')
		elif a!=b!=c:
			print('Scalene')
	elif a==b==c==0:
		A=False	
	else:
		print('Invalid')