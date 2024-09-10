mn,mx = map(int,input().split())
s = set()
x = 2
while x**2<=mx:
    start = (mn + x**2 - 1) // x**2 * x**2
    for i in range(start,mx+1,x**2):
        s.add(i)
    x += 1
print(mx-mn-len(s)+1)