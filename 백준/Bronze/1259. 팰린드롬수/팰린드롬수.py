A=True
while A:
	a1=input()
	a=[]
	a[:]=a1
	if a1=='0':
		A=False
	else:
		if len(a)%2==1:
			c=0
			for i in range(0,(len(a)+1)//2-1,1):
				if a[i]==a[len(a)-1-i]:
					c+=1
			if c==(len(a)+1)//2-1:
				print('yes')
			else:
				print('no')
		else:
			d=0
			for i in range(0,len(a)//2,1):
				if a[i]==a[len(a)-1-i]:
					d+=1
			if d==len(a)//2:
				print('yes')
			else:
				print('no')