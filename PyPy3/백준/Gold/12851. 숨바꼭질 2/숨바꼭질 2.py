from collections import deque

n, k = map(int, input().split())
visited = [False for _ in range(100001)]

q = deque([(n, 0)])
visited[n] = True
res, c = 0, 0

while q:
    now, time = q.popleft()
    visited[now] = True
    if now == k:
        if res == 0:
            res = time
        if time == res:
            c += 1
    
    for next_pos in (now * 2, now + 1, now - 1):
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            q.append((next_pos, time + 1))

print(res)
print(c)