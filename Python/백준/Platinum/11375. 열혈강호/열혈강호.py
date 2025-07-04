import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(n):
    visited[n] = True
    for t in l[n]:
        if v[t] == -1:
            v[t] = n
            return True
        elif not visited[v[t]] and dfs(v[t]):
            v[t] = n
            return True
    return False

n,m = map(int, input().split())
l = [[] for _ in range(n+1)]
v = [-1 for _ in range(m+1)]
for i in range(1,n+1):
    l[i] = list(map(int, input().split()))[1:]

res = 0
for i in range(1,n+1):
    visited = [False] * (n+1)
    if dfs(i):
        res += 1
print(res)