a1=int(input())
a2=input()
a=[]
a[:]=a2
c1='abcdefghijklmnopqrstuvwxyz'
c=[]
c[:]=c1

d=0
for i in range(len(a)):
	d+=(c.index(a[i])+1)*31**i

if 1<=len(a)<=5:
	print (d)
elif 6<=len(a)<=50:
	print(d%1234567891)