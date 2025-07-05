a=input('')
q=[]
w=[]
e=[]

b='abcdefghijklmnopqrstuvwxyz'
q[:]=b
c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
w[:]=c
d='0123456789'
e[:]=d

for i in q:
	if i==a:
		print(q.index(a)+97)
for i in w:
	if i==a:
		print(w.index(a)+65)
for i in e:
	if i==a:
		print(e.index(a)+48)