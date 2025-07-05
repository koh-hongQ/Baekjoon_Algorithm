a=[0,31]
for i in range(28):
	b=int(input())
	a+=[b]
a.sort()

for i in range(29):  #여기서 30이 아니라 29인게 겁나 중요, 30이면 마지막 시행에서 없는 a[i+1]땜에 안됨.
	if a[i+1]-a[i]==2:
		print(a[i]+1)
	elif a[i+1]-a[i]==3:
		print(a[i]+1, end=' ')
		print(a[i]+2)