import sys
input = sys.stdin.readline

def build_spf(n):
    spf = list(range(n+1))
    for i in range(2, int(n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def sol(x, m, spf):
    if x == 1:
        return 0
    tx = 1
    bad = 1
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        tx *= (cnt + 1)
        bad *= (cnt // m + 1)
    return tx - bad - 1

A, B, m = map(int, input().split())
N = A + B
spf = build_spf(N)

ans = 0
for x in range(A, A + B + 1):
    ans += sol(x, m, spf)

print(ans)