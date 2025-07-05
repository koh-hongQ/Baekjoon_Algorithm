a=int(input())
for i in range(a):
	b=int(input())
	c=b//25
	d=(b%25)//10
	e=((b%25)%10)//5
	f=((b%25)%10)%5
	print(c,d,e,f)