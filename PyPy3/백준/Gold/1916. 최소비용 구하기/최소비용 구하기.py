import sys,heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
l = [[] for _ in range(n+1)]
for i in range(m):
    s,d,v = map(int,input().split())
    l[s].append((d,v))
stt,dst = map(int,input().split())

res = [10**10 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
res[stt] = 0

q = [(0,stt)]

while q:
    cost,node = heapq.heappop(q)
    if visited[node]:
        continue
    visited[node] = True

    for d,v in l[node]:
        res[d] = min(cost+v,res[d])
        heapq.heappush(q, (res[d], d))

print(res[dst])