import sys
from collections import deque

a=int(sys.stdin.readline())
c=deque()
for i in range(1,a+1,1):
	c+=[i]


if len(c)==1:
	print(1)
else:
	while len(c)!=1:
		c.popleft()
		if len(c)==1:
			print(c[0])
			break
		else:
			c+=[c.popleft()]