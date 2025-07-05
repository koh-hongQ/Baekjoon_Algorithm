max=0
I=0
J=0
a=[list(map(int, input().split())) for _ in range(9)]
for i in range(9):
	for j in range(9):
		if a[i][j]>max:
			max=a[i][j]
			I=i
			J=j
print (max)
print(I+1, end=' ')
print(J+1)