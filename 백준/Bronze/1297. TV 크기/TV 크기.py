import math

a,b,c = map(int,input().split())

A=math.sqrt(a**2/(b**2+c**2))

h=A*b
if type(h)==float:
	h=int(h)
l=A*c
if type(l)==float:
	l=int(l)

print(h, end=' ')
print(l)
