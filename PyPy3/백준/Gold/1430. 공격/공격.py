import sys,math
input = sys.stdin.readline

n,r,d,x,y = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
enemy = []
res = [[] for _ in range(n)]
q = []
visited = [0]*n
for i in range(n):
    ix,iy = arr[i]
    dist = math.sqrt((x - ix) ** 2 + (y - iy) ** 2)
    if dist <= r:
        enemy.append([i])
        q.append(i)
        visited[i] = 1

while q:
    t = q.pop(0)
    cx,cy = arr[t]
    for i in range(n):
        if visited[i]:
            continue
        ix,iy = arr[i]
        dist = math.sqrt((cx - ix) ** 2 + (cy - iy) ** 2)
        if dist <= r:
            res[t].append(i)
            q.append(i)
            visited[i] = 1

s = 0
def attack(t,level):
    global s
    s += d/(2**level)
    for i in res[t]:
        attack(i,level+1)

for i in enemy:
    attack(i[0],0)
print(s)