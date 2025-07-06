def dfs(n,path):
    if n==end:
        res.append(len(path)-1)
        return
    for i in l[n]:
        if i not in path:
            dfs(i,path+[i])

n = int(input())
l = [[] for _ in range(n+1)]
res = []
start,end = list(map(int,input().split()))
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

dfs(start,[start])
if res:
    print(min(res))
else:
    print(-1)