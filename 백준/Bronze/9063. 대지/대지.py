a=int(input())
b1=[]
c1=[]
for i in range(a):
	b,c=map(int,input().split())
	b1+=[b]
	c1+=[c]
print((max(b1)-min(b1))*(max(c1)-min(c1)))