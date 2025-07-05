x=input()
y=input()
nx=len(x)
ny=len(y)
# c=[[0]*(n+1)]*(n+1)
# for i in range(n):
# 	c[i][0]=0
# for i in range(n):
# 	c[0][i]=0

c= [[0] * (ny + 1) for _ in range(nx+ 1)]
	
for i in range(1,nx+1):
	for j in range(1,ny+1):
		if x[i-1]==y[j-1]:
			c[i][j]=c[i-1][j-1]+1
		else:
			c[i][j]=max(c[i-1][j],c[i][j-1])
print(max(max(c)))