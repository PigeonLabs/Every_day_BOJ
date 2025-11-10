import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
maxtree, mintree = [nums], [nums]
i = 1
while (1<<i) <= n:
    maxtree.append([max(maxtree[i-1][2*j], maxtree[i-1][2*j+1]) for j in range(len(maxtree[i-1])//2)])
    mintree.append([min(mintree[i-1][2*j], mintree[i-1][2*j+1]) for j in range(len(mintree[i-1])//2)])
    i += 1

def segrange(a, b):
    res = []
    while a <= b:
        lsb = (a - 1) & -(a - 1)
        if lsb == 0:
            lsb = 1 << ((b - a + 1).bit_length() - 1)
        while a + lsb - 1 > b:
            lsb >>= 1
        res.append((a, a + lsb - 1))
        a += lsb
    return res

for _ in range(m):
    a,b = map(int, input().split())
    mn = 10**9+1
    mx = 0
    for s,e in segrange(a, b):
        k = (e - s + 1).bit_length() - 1
        mn = min(mn, mintree[k][(s - 1) >> k])
        mx = max(mx, maxtree[k][(s - 1) >> k])
    print(mn,mx)