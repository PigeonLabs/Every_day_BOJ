import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
rev_graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

visited = [False] * (v+1)
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
for i in range(1, v+1):
    if not visited[i]:
        dfs1(i)

# 2차 DFS: 역그래프에서 SCC 추출
visited = [False] * (v+1)
sccs = []

while order:
    node = order.pop()
    if not visited[node]:
        comp = []
        dfs2(node, comp)
        sccs.append(comp)

print(len(sccs))
for comp in sorted(sccs, key=lambda x: min(x)):
    print(*(sorted(comp) + [-1]))