a=int(input())

for i in range(a):
	print(' '*(a-1-i), end='')
	print('*'*(2*i+1))
for j in range(a-1):
	print(' '*(j+1), end='')
	print('*'*(2*(a-1)-(2*j+1)))