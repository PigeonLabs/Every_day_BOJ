import sys
input = sys.stdin.readline

n = int(input())
l = []
v = 0
for _ in range(n):
    d,w = map(int, input().split())
    l.append((d-1, w))
    v = max(v, d-1)
l.sort(key=lambda x: (x[1], x[0]),reverse=True)
res = [0 for _ in range(v+1)]
for i in l:
    for x in range(i[0], -1, -1):
        if res[x] == 0:
            res[x] = i[1]
            break
print(sum(res))