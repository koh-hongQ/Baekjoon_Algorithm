import sys

a=int(input())
c=list(map(int, sys.stdin.readline().split()))

b=1000000
d= -1000000

for i in c:
	if i<b:
		b=i

for i in c:
	if i>d:
		d=i


print(b, end=' ')
print(d)