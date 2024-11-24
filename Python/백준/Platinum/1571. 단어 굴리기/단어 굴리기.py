import sys,math,itertools
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extended_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y

def crt(a1, m1, a2, m2):
    g, p, q = extended_gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None
    lcm = m1 * m2 // g
    t = (a1 + (a2 - a1) // g * p * m1) % lcm
    return t, lcm

n = int(input())
l = [input().strip() for _ in range(n)]
dst = input().strip()

leng = [len(s) for s in l]
loc = []
for i in range(n):
    pos = [x for x, ch in enumerate(l[i]) if ch == dst[i]]
    if not pos:
        print(-1)
        exit()
    loc.append(pos)

res = 10**20
for comb in list(itertools.product(*loc)):
    time = comb[0]
    step = leng[0]
    possible = True
    for i in range(1,n):
        result = crt(time, step, comb[i], leng[i])
        if result is None:
            possible = False
            break
        time, step = result
    if possible:
        res = min(res,time)

if res == 10**20:
    print(-1)
else:
    print(res)