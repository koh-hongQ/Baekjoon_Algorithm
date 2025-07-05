import math

A=int(input())
for i in range(A):
	a,b=map(int,input().split())
	q=max(a,b)
	w=min(a,b)
	print(int(math.factorial(q)/(math.factorial(w)*math.factorial(q-w))))