
a=list(map(int,input().split()))
c=min(a[2]-a[0],a[0])
d=min(a[3]-a[1],a[1])
print(min(c,d))