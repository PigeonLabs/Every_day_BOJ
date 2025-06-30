import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    v = [0] + list(map(int, input().split()))
    prev = [[] for _ in range(n+1)]
    dp = [-1]*(n+1)
    for _ in range(k):
        a,b = map(int, input().split())
        prev[b].append(a)
    w = int(input())

    def f(x):
        if dp[x] != -1:
            return dp[x]
        if not prev[x]:
            dp[x] = v[x]
        else:
            dp[x] = max(f(p) for p in prev[x]) + v[x]
        return dp[x]
    
    print(f(w))