import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    k1 = list(map(str, input().split()))
    k2 = list(map(str, input().split()))
    pos = {val: i for i, val in enumerate(k2)}
    x = {i: pos[k1[i]] for i in range(n)}
    v = list(map(str, input().split()))
    res = [v[x[i]] for i in range(n)]
    print(' '.join(res))
