a= int(input())
b=list(map(int, input().split()))

m=0
for i in b:
	if i>m:
		m=i

s=[]
for i in b:
	s+=[(i/m)*100]

k=0	
for i in s:
	k+=i
print(k/len(s))