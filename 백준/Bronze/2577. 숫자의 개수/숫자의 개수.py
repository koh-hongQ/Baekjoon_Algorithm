a=''
c=1
for i in range(3):
	b=input()
	c=c*int(b)
a+=str(c)


p=[]
for i in range(len(a)):
	p+=[a[i]]
for i in range(10):
	print(p.count(str(i)))