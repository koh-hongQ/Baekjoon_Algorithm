a1=input()
a2=a1.upper()
a=[]
a[:]=a2
b=set(a)

max=0
l=0
k=''
k1=''
for i in b:
	if a.count(i)>max:
		max=a.count(i)
		k=i
	elif a.count(i)==max:
		k1=k


if k==k1:
	print('?')
else:
	print(k)