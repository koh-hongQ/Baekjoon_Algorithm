c=[]
for i in range(5):
	a=int(input())
	if a<40:
		c+=[40]
	else:
		c+=[a]
print(int(sum(c)/5))






