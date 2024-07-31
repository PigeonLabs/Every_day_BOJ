from itertools import permutations as p

n = int(input())
l = list(map(int,input().split()))
l = set(p(l))
ans = 0

for k in l:
    res = [0]
    res2 = set()
    for i in range(n):
        res.append(k[i]+res[-1])
        res2.add(k[i]+res[-2]+50)
    ans = max(len(set(res)&res2),ans)

print(ans)