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
	print(a+b+c)
elif a+b<=c:
	print(a+b+(a+b-1))