import sys
input = sys.stdin.readline

def profit(a, b, ea, eb):
    res = l[ea][eb]
    if a > 0:
        res -= l[a-1][eb]
    if b > 0:
        res -= l[ea][b-1]
    if a > 0 and b > 0:
        res += l[a-1][b-1]
    return res

def get_region_sums(a, b, ea, eb):
    sums = {}
    if a > ea or b > eb:
        return sums
    for i in range(a, ea+1):
        for j in range(b, eb+1):
            for k in range(i, ea+1):
                for m in range(j, eb+1):
                    s = profit(i, j, k, m)
                    sums[s] = sums.get(s, 0) + 1
    return sums

n = int(input())
l = [[0] * n for _ in range(n)]
for i in range(n):
    t = list(map(int, input().split()))
    l[i][0] = t[0]
    for j in range(1, n):
        l[i][j] = l[i][j-1] + t[j]
for i in range(1, n):
    for j in range(n):
        l[i][j] += l[i-1][j]

ans = 0
for a in range(0, n-1):
    for b in range(0, n-1):
        d1 = {}
        for r in range(0, a+1):
            for c in range(0, b+1):
                s_val = profit(r, c, a, b)
                d1[s_val] = d1.get(s_val, 0) + 1
        d2 = {}
        for r in range(a+1, n):
            for c in range(b+1, n):
                s_val = profit(a+1, b+1, r, c)
                d2[s_val] = d2.get(s_val, 0) + 1
        for s_val in d1:
            if s_val in d2:
                ans += d1[s_val] * d2[s_val]

for r in range(0, n-1):
    for c in range(1, n):
        d1 = {}
        for r1 in range(0, r+1):
            for c2 in range(c, n):
                s_val = profit(r1, c, r, c2)
                d1[s_val] = d1.get(s_val, 0) + 1
        d2 = {}
        for r2 in range(r+1, n):
            for c1 in range(0, c):
                s_val = profit(r+1, c1, r2, c-1)
                d2[s_val] = d2.get(s_val, 0) + 1
        for s_val in d1:
            if s_val in d2:
                ans += d1[s_val] * d2[s_val]

print(ans)