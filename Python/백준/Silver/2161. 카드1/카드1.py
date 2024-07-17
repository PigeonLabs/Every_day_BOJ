from collections import deque
l = deque([x+1 for x in range(int(input()))])
while l:
    print(l.popleft(),end=" ")
    l.rotate(-1)