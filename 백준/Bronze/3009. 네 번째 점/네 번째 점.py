a1=[]
b1=[]
A=0
B=0
for i in range(3):
	a,b=map(int,input().split())
	a1+=[a]
	b1+=[b]
for i in range(3):
	if a1.count(a1[i])==1:
		A=a1[i]
for i in range(3):
	if b1.count(b1[i])==1:
		B=b1[i]
print(A, end=' ')
print(B)