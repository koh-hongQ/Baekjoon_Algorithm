a=int(input())
def f(a):
	a1=1
	for i in range(a):
		a1=a1*(i+1)
	return a1
b=f(a)
c=[]
c[:]=str(b)
c.reverse()

d=0

for i in range(len(c)):
	if c[i]=='0':
		d+=1
	elif c[i]!='0':
		print(d)
		break