A=int(input())
c=[]
for i in range(A):
	a,b=map(int,input().split())
	c.append([a,b])

c.sort(key=lambda x: (x[0],x[1]))
for i in c:
	print(i[0],i[1])