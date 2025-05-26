import sys
import math
input = sys.stdin.readline

n = int(input())
l = sorted(map(int, input().split()), reverse=True)
m = int(input())

total = sum(l)
removed = 0
idx = 0

while idx + 1 < n:
    delta_h = l[idx] - l[idx+1]
    if removed + delta_h * (idx+1) >= total - m:
        break
    removed += delta_h * (idx+1)
    idx += 1

c = l[idx]
need = max(total - m - removed, 0)
cut = math.ceil(need / (idx+1))

answer_height = c - cut
print(answer_height)