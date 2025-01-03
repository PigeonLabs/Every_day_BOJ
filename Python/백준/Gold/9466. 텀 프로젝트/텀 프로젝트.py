import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, team):
    visited[x] = True
    path.append(x)
    next_node = l[x]
    
    if visited[next_node]:
        if next_node in path:
            team += path[path.index(next_node):]
        return
    else:
        dfs(next_node, team)

for _ in range(int(input())):
    cn = int(input())
    l = [0] + list(map(int, input().split()))
    visited = [False] * (cn + 1)
    team = []
    
    for i in range(1, cn + 1):
        if not visited[i]:
            path = []
            dfs(i, team)
    
    print(cn - len(team))