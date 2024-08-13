g = int(input())

res = []
for a in range(int(g**.5)+1,50001):
    t = (a**2-g)**.5
    if t == int(t):
        res.append(a)
if res:
    for i in res:
        print(i)
else:
    print(-1)