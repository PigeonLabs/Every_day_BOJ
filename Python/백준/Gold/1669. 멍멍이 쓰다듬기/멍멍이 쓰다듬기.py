x,y = map(int,input().split())
t = y-x
if t==0:
    print(0)
    exit()
p = 2
pv = 1
while p**2 < t:
    pv = p
    p *= 2
while pv < p:
    m = (p+pv)//2
    if t<=m**2:
        p = m-1
    else:
        pv = m+1

p = pv-1
while True:
    if t==p**2:
        print(2*p-1)
        break
    elif p**2<t<=p*(p+1):
        print(2*p)
        break
    elif p*(p+1)<t<(p+1)**2:
        print(2*p+1)
        break
    p += 1