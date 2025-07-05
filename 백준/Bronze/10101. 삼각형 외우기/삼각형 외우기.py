a=int(input())
b=int(input())
c=int(input())

if a==60 and b==60 and c==60:
	print('Equilateral')
elif a+b+c==180 and a==b and b!=c:
	print('Isosceles')
elif a+b+c==180 and c==b and a!=c:
	print('Isosceles')
elif a+b+c==180 and a==c and b!=a:
	print('Isosceles')
elif a+b+c==180 and a!=b!=c:
	print('Scalene')
else:
	print('Error')