A=input()
f=0

if int(A)<10:
	A+='0'
	a=A
else:
	a=A


while True:
	
	a1=str(int(a[0])+int(a[1]))
	b=a[1]+a1[-1]
	f+=1
	if A==b:
		break
	a=b
print(f)