a,b=map(str, input().split())
b=int(b)
a1=[]
a1[:]=a

for i in range(len(a1)):
	if 65<=ord(a1[i])<=90:
		a1[i]=ord(a1[i])-55


c=0
for i in range(len(a1)):
	c+=(b**i)*int(a1[len(a1)-1-i])
print(c)


