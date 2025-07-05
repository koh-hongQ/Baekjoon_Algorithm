a,b= map(int, input().split())
p=[]
for i in range(a):
	p+=[i+1]
	
f=0
for i in range(b):
	c,d=map(int, input().split())
	f=p[c-1]
	p[c-1]=p[d-1]
	p[d-1]=f
	
for i in range(a):
	print(p[i],end=' ' )