n, x = map(int, input().split())
res = []

a = False
if n<0 and 0<x:
    a = True
    n = -n

if x < 0:
    while n != 0:
        r = n % x
        n = n // x
        if r < 0:
            r -= x
            n += 1
        res.append(r)
else:
    while n != 0:
        res.append(n % x)
        n //= x

res.reverse()
if res:
    if a:
        print("-" + "".join(map(str, res)))
    else:
        print("".join(map(str, res)))
else:
    print(0)