a=int(input())

for i in range(a):
	k=int(input())
	n=int(input())
	
	zerofloor=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	floor=[0]*n

	for i in range (k):
		d=0
		for i in range(n):
			d+=zerofloor[i]
			floor[i]=d
		zerofloor=floor
	print(floor[n-1])