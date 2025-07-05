a=input()

a1=[]
a1[:]=a

l='abcdefghijklmnopqrstuvwxyz'
l1=[]
l1[:]=l

f=[]
for i in range(len(l1)):
	f+=[-1]

for i in l1:
	for j in a1:
		if i==j:
			f[l1.index(i)]=a1.index(j)


for i in f:
	print(i, end=' ')