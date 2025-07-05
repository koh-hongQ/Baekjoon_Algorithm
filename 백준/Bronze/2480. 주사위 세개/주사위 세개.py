a,b,c=map(int, input().split())


def maxFunc(A):
	max = 0
	for i in range(len(A)):
		if A[i] > max:	
			max = A[i]
	return max

A = [a,b,c] 
maxNum = maxFunc(A)

if a==b and b==c and a==c:
  print(10000+a*1000)
elif a==b and b!=c:
	print(1000+a*100)
elif a==c and a!=b:
	print(1000+a*100)
elif b==c and a!=c:
  print(1000+b*100)
else:
	print(maxNum*100)
	