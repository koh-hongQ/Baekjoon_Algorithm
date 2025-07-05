a=int(input())
b=int(input())
f=0
for i in range(b):
	c,d=map(int, input().split())
	f+=c*d
if a==f:
	print('Yes')
else:
	print('No')