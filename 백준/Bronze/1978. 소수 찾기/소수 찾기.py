t=int(input())
p=list(map(int, input().split()))




import math
b=0 #b는 소수 아닌 놈의 개수
for i in p:
	if i==1:
		b+=1
	else:
		for j in range(2,int(math.sqrt(i))+1,1):
			if i%j==0:
				b+=1
				break
print(t-b)