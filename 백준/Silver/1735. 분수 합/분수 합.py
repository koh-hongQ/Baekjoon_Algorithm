a,b=map(int,input().split())
c,d=map(int,input().split())
def f(a,b): #최대공배수
	a1=a
	b1=b
	while True:
		d=a%b
		if d==0:
			break
		a=b
		b=d
	return int(a1*b1/b)

def g(a,b): #최대공약수
	a1=a
	b1=b
	while True:
		d=a%b
		if d==0:
			break
		a=b
		b=d
	return b

bunmo=f(b,d)
bunja=a*(bunmo/b)+ c*(bunmo/d)
last=g(bunmo,bunja)
print(int(bunja/last), int(bunmo/last))