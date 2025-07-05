import math
c=[] #a의 약수 넣기
d=[] #a의 약수 중 소수만 넣기
a=int(input())
for i in range(1,a+1,1):
	if a%i==0:
		c+=[i]
for i in c:
	if i==1:
		continue
	else:
		b=0
		for j in range(2,int(math.sqrt(i))+1,1):
			if i%j==0:
				b+=1
				break
		if b==0:
			d+=[i]
for i in d: #d의 각 소수 개수를 찾기(a를 각 소수로 계속 나누면서)
	p=0
	A=True
	while A:
		p+=1
		a=a//i
		if a%i!=0:
			A=False
	for j in range(p):
		print(i)