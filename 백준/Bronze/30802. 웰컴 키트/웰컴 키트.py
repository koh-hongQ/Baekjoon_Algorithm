a=int(input())
c=list(map(int,input().split()))
b1,b2=map(int,input().split())


c1=0
for i in c:
	if i==0:
		f=0
	else:
		if i%b1==0:
			f=i//b1
		else:
			f=i//b1+1
	c1+=f

print(c1)
print(a//b2, a%b2)