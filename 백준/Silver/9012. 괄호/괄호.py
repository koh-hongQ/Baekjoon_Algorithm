A=int(input())
for i in range(A):


	a=input()
	c=[]
	c[:]=a
	d=[]
	x=0
	for i in range(len(c)):
		if c[i] =='(':
			d+=['(']
		elif c[i] ==')':
			if len(d)==0:
				x+=1
			else:
				d.pop()
				x+=1
	if len(d)==0 and x==len(c)//2:
		print('YES')
	else:
		print('NO')