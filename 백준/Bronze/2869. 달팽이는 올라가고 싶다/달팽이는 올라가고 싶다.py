a,b,c=map(int,input().split())

if (c-b)%(a-b)==0:
	c=(c-b)/(a-b)
elif (c-b)%(a-b)!=0:
	c=(c-b)/(a-b)+1
print(int(c))