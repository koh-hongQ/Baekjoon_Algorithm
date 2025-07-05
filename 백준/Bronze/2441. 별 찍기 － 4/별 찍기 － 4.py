a=int(input())
for i in range(1,a+1,1):
	for j in range(i-1):
		print(' ', end='')
	print('*'*(a-i+1))