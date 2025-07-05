a,b=map(str, input().split())

a1=[]
a1[:]=a
a1.reverse()
a3=int(a1[0])*100+int(a1[1])*10+int(a1[2])

b1=[]
b1[:]=b
b1.reverse()
b3=int(b1[0])*100+int(b1[1])*10+int(b1[2])

if a3>b3:
	print(a3)
else:
	print(b3)