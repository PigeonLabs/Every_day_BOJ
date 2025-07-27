import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
sorted_items = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
print(sorted_items[0][0])