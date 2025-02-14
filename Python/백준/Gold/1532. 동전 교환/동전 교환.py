s = list(map(int, input().split()))
d = list(map(int, input().split()))
res = 0

if d[2]>s[2]:
    t = (d[2]-s[2]+8)//9
    s[1] -= t
    s[2] += t*9
    res += t
if d[1]>s[1] and s[0]>d[0]:
    t = min(s[0]-d[0],(d[1]-s[1]+8)//9)
    s[0] -= t
    s[1] += t*9
    res += t
if d[0]>s[0]:
    t = d[0]-s[0]
    s[1] -= t*11
    s[0] += t
    res += t
if d[1]>s[1]:
    t = d[1]-s[1]
    s[2] -= t*11
    s[1] += t
    res += t
if any(dv > sv for sv, dv in zip(s, d)):
    print(-1)
else:
    print(res)