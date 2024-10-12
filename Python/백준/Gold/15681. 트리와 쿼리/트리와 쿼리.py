import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N,R,Q = map(int,input().split())

m=[[]for _ in range(N+1)]
visit=[0 for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    m[a].append(b)
    m[b].append(a)

def dfs(now):
    global visit
    visit[now]=1
    for i in m[now]:
        if not visit[i]:
            visit[now]+=dfs(i)
    return visit[now]

dfs(R)

for _ in range(Q):
    get=int(input())
    print(visit[get])