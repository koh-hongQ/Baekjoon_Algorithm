a=int(input())

for i in range(a):
	answer = input('')
	b=answer.split('X')
	total = 0


	for i in range(len(answer)):
		total+=(i+1)*(i+2)/2*b.count('O'*(i+1))

	print(int(total))