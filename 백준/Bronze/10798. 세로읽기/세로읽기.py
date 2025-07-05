a=[list(map(str,input())) for _ in range(5)]
max=0
for i in a:
	if len(i)>max:
		max=len(i)

for i in range(max):
	for j in range(5):
		if len(a[j])<max and i>=len(a[j]):
			continue
		print(a[j][i],end='')