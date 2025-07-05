a,b= map(int, input().split())
p=[]
for i in range(a):
	p+=[0]

for i in range(b):
	c,d,e=map(int, input().split())
	
	for i in range(c,d+1,1):
		p[i-1]=e
		
for i in range(a):
	print(p[i],end=' ' )