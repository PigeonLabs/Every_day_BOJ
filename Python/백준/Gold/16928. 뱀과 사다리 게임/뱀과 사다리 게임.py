import sys
input = sys.stdin.readline
from collections import deque

l = [0 for _ in range(101)]
visited = [False for _ in range(101)]

ladder = {}
snake = {}
location = 1

n, m = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

q = deque([location])
visited[location] = True

while q:
    t = q.popleft()
    for i in range(1, 7):
        new_loc = t + i
        if new_loc > 100:
            continue
        
        if new_loc in ladder:
            new_loc = ladder[new_loc]
        elif new_loc in snake:
            new_loc = snake[new_loc]
        
        if not visited[new_loc]:
            visited[new_loc] = True
            l[new_loc] = l[t] + 1
            q.append(new_loc)
        
        if new_loc == 100:
            print(l[100])
            exit()

print(l[100])