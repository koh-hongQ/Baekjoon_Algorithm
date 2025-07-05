a=int(input())

c1=[]
for i in range(a):
	b,c=map(str, input().split())
	c1[:]=c
	for j in c1:
		print(j*int(b), end='')
	print('')