import sys
input = sys.stdin.readline
a=int(sys.stdin.readline())

for i in range(a):
	b,c=map(int, input().split())
	print('Case #%d: %d' %(i+1, b+c))
