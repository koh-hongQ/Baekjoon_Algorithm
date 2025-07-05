a=input()
a1=[]
a1[:]=a

b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c='22233344455566677778889999'
b1=[]
b1[:]=b

c1=[]
c1[:]=c

d=0
for i in a1:
	d+=int(c1[b.index(i)])
print(d+len(a1))