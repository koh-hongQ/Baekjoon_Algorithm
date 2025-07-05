a1= input()
a=[]
a[:]=a1

b=0
c=0
if len(a)%2==1:
	for i in range(0,(len(a)+1)//2-1,1):
		if a[i]==a[len(a)-1-i]:
			b+=1
	if b==(len(a)+1)//2-1:
		print(1)
	else:
		print(0)

else:
	for i in range(0,(len(a))//2,1):
		if a[i]==a[len(a)-1-i]:
			c+=1
	if c==(len(a))//2:
		print(1)
	else:
		print(0)