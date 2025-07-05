import math


def f (a):
	b=0
	for i in range(2,int(math.sqrt(a))+1,1):
		if a%i==0:
			b+=1
			break
	if b==0:
		return a
	else:
		return 


a,b=map(int,input().split())
if a==1 and b!=1:
	for i in range(a+1,b+1,1):
		if type(f(i))==int:
			print(f(i))
elif a!=1 and b!=1:
	for i in range(a,b+1,1):
		if type(f(i))==int:
			print(f(i))