a=int(input())
b=0
c=0
A=True
while A:
	if a==1:
		print('1/1')
		A=False
	else:
		for i in range(10000):
			if (i**2)/2-i/2+1==a:
				if i%2==0:
					print('1/%d' %i)
					A=False
				else:
					print('%d/1' %i)
					A=False
			else:
				if ((i-1)**2)/2-(i-1)/2+1<a<(i**2)/2-i/2+1:
					b=i-1
					c=a-(((i-1)**2)/2-(i-1)/2+1)
					if b%2==0:
						print('%d/%d'   %((1+c),(i-1-c)))
					else:
						print('%d/%d'   %((i-1-c),(1+c)))
					A=False