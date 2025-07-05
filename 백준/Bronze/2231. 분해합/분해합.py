b=int(input())
c=[]
for i in range(1000000):
	i1=[]
	i1[:]=str(i)
	i1+=[str(i)]
	d=0
	for j in i1:
		d+=int(j)
	if d==b:  #b가 100자리 이상의 수면?
		c+=[i]
if c==[]:
	print(0)
else:
	print(min(c))