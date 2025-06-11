import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    l = []
    w = input().strip()
    for i in range(len(w)):
        l.append(w[i:] + w[:i])
    l.sort()
    s.add(l[0])
print(len(s))