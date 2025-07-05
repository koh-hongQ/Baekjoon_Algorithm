c=[1,1,1,2,2]
for i in range(100):
	c+=[c[i]+c[i+4]]

A=int(input())
for i in range(A):
	b=int(input())
	print(c[b-1])