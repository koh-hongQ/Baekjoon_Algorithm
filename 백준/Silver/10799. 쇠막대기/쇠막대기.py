a=input()
c=[]
c[:]=a
d=[]
x=0
for i in range(len(c)):
	if c[i] =='(':
		d+=['(']
	elif c[i] ==')':
		if c[i-1]=='(':
			d.pop() #레이저를 제외하고 쌓인 스택 만큼 더하기. 즉 스택-1 만큼 더하기
			x+=len(d)
		elif c[i-1]==')':
			d.pop() #pop하는 이유는, 이미 끝난 막대이므로, 나중에 레이저쏴서 스택-1만큼 더할때, 거기서 제외하기 위함
			x+=1
print(x)