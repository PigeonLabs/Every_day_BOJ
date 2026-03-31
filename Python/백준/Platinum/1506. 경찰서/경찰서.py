import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]

cost = list(map(int, input().split()))
for i in range(n):
    arr = list(map(int, list(input().strip())))
    for j in range(n):
        if arr[j] == 1:
            graph[i].append(j)
            rev_graph[j].append(i)

visited = [False] * (n)
order = []

def dfs1(node):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs1(nxt)
    order.append(node)

def dfs2(node, comp):
    visited[node] = True
    comp.append(node)
    for nxt in rev_graph[node]:
        if not visited[nxt]:
            dfs2(nxt, comp)

# 1차 DFS: 종료 순서 저장
for i in range(n):
    if not visited[i]:
        dfs1(i)

# 2차 DFS: 역그래프에서 SCC 추출
visited = [False] * (n)
sccs = []

while order:
    node = order.pop()
    if not visited[node]:
        comp = []
        dfs2(node, comp)
        sccs.append(comp)

res = 0
for i in sccs:
    res += min(cost[x] for x in i)
print(res)