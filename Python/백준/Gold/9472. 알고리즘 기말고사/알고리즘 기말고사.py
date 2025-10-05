import sys,math
input = sys.stdin.readline

def solve(n, k):
    res = 0
    for i in range(k + 1):
        term = math.comb(k, i) * math.factorial(n - i)
        if i % 2 == 0:
            res += term
        else:
            res -= term
    return res

t = int(input())
for _ in range(t):
    x,n,k = map(int, input().split())
    print(x, solve(n, k))