try:
	[...]
except:
	[...]


c=True
while c:
	try:
		a,b=map(int, input().split())
		print(a+b)
	except:
		break
