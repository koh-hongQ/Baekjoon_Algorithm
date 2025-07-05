b1=0
d=0
for i in range(20):
	a,b,c=map(str,input().split())
	if c!='P':
		c=c.replace('A+', '4.5')
		c=c.replace('A0', '4.0')
		c=c.replace('B+', '3.5')
		c=c.replace('B0', '3.0')
		c=c.replace('C+', '2.5')
		c=c.replace('C0', '2.0')
		c=c.replace('D+', '1.5')
		c=c.replace('D0', '1.0')
		c=c.replace('F', '0.0')
		b1+=float(b)
		d+=float(b)*float(c)
	else:
		b1+=0
		d+=0
	
print('%.6f' %(d/b1))