n = int(input())
l = list(map(int,input().split()))
t = int(input())

tree = [[] for _ in range(n)]
for i in range(n):
    if l[i]>=0:
        tree[l[i]].append(i)
root = l.index(-1)

if t==root:
    print(0)
    exit()

def dfs1(n):
    for i in tree[n][:]:
        dfs1(i)
        tree[n].remove(i)

res = 0
def dfs2(n):
    global res
    if len(tree[n])==0:
        res += 1
        return
    for i in tree[n]:
        dfs2(i)

dfs1(t)
if t in tree[l[t]]:
    tree[l[t]].remove(t)
dfs2(root)
print(res)