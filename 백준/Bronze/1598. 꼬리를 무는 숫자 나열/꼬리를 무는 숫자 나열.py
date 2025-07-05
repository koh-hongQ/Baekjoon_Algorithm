a,b=map(int,input().split())
A=0
B=0
if a%4==1:
	na=(a+3)/4
	A=3
elif a%4==2:
	na=(a+2)/4
	A=2
elif a%4==3:
	na=(a+1)/4
	A=1
elif a%4==0:
	na=(a)/4
	A=0


if b%4==1:
	nb=(b+3)/4
	B=3
elif b%4==2:
	nb=(b+2)/4
	B=2
elif b%4==3:
	nb=(b+1)/4
	B=1
elif b%4==0:
	nb=(b)/4
	B=0


print(int(abs(na-nb)+abs(A-B)))