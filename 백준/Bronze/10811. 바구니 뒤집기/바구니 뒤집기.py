a,b = map(int, input().split())
c=[]
for i in range(a):
	c+=[i+1]
	

for i in range(b):
	d,e = map(int, input().split())
	w=[]
	for j in range(d-1,e,1):
		w+=[c[j]]
	w.reverse()
	c[d-1:e]=w
	w=[]
	
for i in range(len(c)):
	print(c[i], end=' ')
