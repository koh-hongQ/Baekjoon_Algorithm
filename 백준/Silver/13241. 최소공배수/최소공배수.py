a,b=map(int,input().split())
a1=a
b1=b
while True:
	d=a%b
	if d==0:
		break
	a=b
	b=d
print(int(a1*b1/b))