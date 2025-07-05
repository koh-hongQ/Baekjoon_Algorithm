t=0
w=int(input())
for i in range(w):
	a=input()
	c=[]
	c[:]=a
	d=c
	k=''
	for i in range(len(c)-1):
		if c[i+1]!=c[i]:
			d[i]+='A'
		k+=d[i]
	k+=d[len(c)-1]
	k=k.split('A')

	for i in range(len(k)):
		if len(k[i])>1:
			k[i]=k[i][0]
	for i in range(len(k)):
		if k.count(k[i])>1:
			t+=1
			break
print(w-t)