
import sys
from collections import deque

a,b=map(int,sys.stdin.readline().split())

Q=deque()
c=[]
for i in range(1,a+1):
    Q.append(i)
while Q:
    for i in range(1,b):
        Q.append(Q.popleft())
    c.append(Q.popleft())
# c+=[Q[0]]
if len(c)==1:
    print('<1>')
else:
    for i in range(len(c)):
        if i==0:
            print('<' , end='')
            print(c[0], end=', ')
        elif i==len(c)-1:
            print(c[len(c)-1], end='')
            print('>')
            
        else:
            print(c[i], end=', ')