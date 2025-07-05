a,b=map(int,input().split())
c1=[list(map(int,input().split())) for _ in range(a)]
c2=[list(map(int,input().split())) for _ in range(a)]

for i in range(a):
	for j in range(b):
		print(c1[i][j]+c2[i][j], end=' ')
	print('')