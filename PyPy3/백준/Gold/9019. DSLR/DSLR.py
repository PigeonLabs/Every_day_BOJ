import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    visited = [False] * 10000
    queue = deque([(a, "")])
    
    while queue:
        current, op = queue.popleft()
        
        if current == b:
            print(op)
            return
        
        # D
        da = (current * 2) % 10000
        if not visited[da]:
            visited[da] = True
            queue.append((da, op + "D"))

        # S
        sa = current - 1 if current > 0 else 9999
        if not visited[sa]:
            visited[sa] = True
            queue.append((sa, op + "S"))

        # L
        la = int(str(current).zfill(4)[1:] + str(current).zfill(4)[0])
        if not visited[la]:
            visited[la] = True
            queue.append((la, op + "L"))

        # R
        ra = int(str(current).zfill(4)[-1] + str(current).zfill(4)[:-1])
        if not visited[ra]:
            visited[ra] = True
            queue.append((ra, op + "R"))

for _ in range(int(input().strip())):
    a, b = map(int, input().strip().split())
    bfs(a, b)