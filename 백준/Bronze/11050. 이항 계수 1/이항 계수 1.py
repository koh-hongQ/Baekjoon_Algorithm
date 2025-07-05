a,b=map(int,input().split())
a1=1

def f (a):
	a1=1
	for i in range(a):
		a1=a1*(i+1)
	return a1


print (int(f(a)/(f(a-b)*f(b))))