from itertools import combinations
a,b=map(int,input().split())
c=list(map(int,input().split()))
max=9
for i in combinations(c,3):
	if b>=sum(i)>max:
		max=sum(i)
print(max)
