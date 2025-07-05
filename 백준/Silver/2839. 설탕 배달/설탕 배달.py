n=int(input())
min=10000
for i in range(5000//3+1):
	for j in range(5000//5+1):
		if n==3*i+5*j and i+j<min:
			min=i+j
if min==10000:
	print(-1)
else:
	print(min)