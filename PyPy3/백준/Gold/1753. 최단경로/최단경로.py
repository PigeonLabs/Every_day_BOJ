import sys,heapq
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
l = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    l[a].append((b, c))

dist = [float('INF')] * (v+1)
dist[s] = 0
q = [(0, s)]

while q:
    udist, u = heapq.heappop(q)
    if udist > dist[u]:
        continue
    for dst,w in l[u]:
        distance = udist + w
        if distance < dist[dst]:
            dist[dst] = distance
            heapq.heappush(q, (distance, dst))

for i in range(1, v+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])