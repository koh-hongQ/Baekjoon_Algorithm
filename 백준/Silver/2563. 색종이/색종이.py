c=[[0]*100 for _ in range(100)]
A=int(input())
p=0
for i in range(A):
	d,e=map(int,input().split())
	for j in range(d,d+10,1):
		for k in range(e,e+10,1):
			if c[j][k]!=1:
				c[j][k]=1
				p+=1

print(p)