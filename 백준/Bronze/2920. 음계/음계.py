a=list(map(int,input().split()))
b=[1,2,3,4,5,6,7,8]
b1=0
c=[8,7,6,5,4,3,2,1]
c1=0

for i in range(len(a)):
	if a[i]==b[i]:
		b1+=1
	elif a[i]==c[i]:
		c1+=1

if b1==8:
	print('ascending')
	
if c1==8:
	print('descending')
	
if b1!=8 and c1!=8:
	print('mixed')
	