from collections import deque
import sys
a=int(sys.stdin.readline())

c=deque([])
for i in range(a):
	b=sys.stdin.readline().split()
	
	if b[0]=='push':
		c+=[b[1]]
	elif b[0]=='pop':
		if len(c)==0:
			print(-1)
		else:
			print(c[0])
			del c[0]
	
	elif b[0]=='size':
		print(len(c))
	
	elif b[0]=='empty':
		if len(c)==0:
			print(1)
		else:
			print(0)
	
	elif b[0]=='front':
		if len(c)==0:
			print(-1)
		else:
			print(c[0])
	elif b[0]=='back':
		if len(c)==0:
			print(-1)
		else:
			print(c[len(c)-1])