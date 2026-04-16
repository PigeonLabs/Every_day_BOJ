import sys
input = sys.stdin.readline

def update(i, v):
    while i <= n:
        tree[i] += v
        i += i & -i

def prefix_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

n = int(input())
arr = [0] + list(map(int, input().split()))

m = int(input())
queries = [[] for _ in range(n + 1)]
for idx in range(m):
    l, r = map(int, input().split())
    queries[r].append((l, idx))

tree = [0] * (n + 1)
last = {}
ans = [0] * m

for i in range(1, n + 1):
    x = arr[i]

    if x in last:
        update(last[x], -1)

    update(i, 1)
    last[x] = i

    for l, idx in queries[i]:
        ans[idx] = prefix_sum(i) - prefix_sum(l - 1)

print(*ans, sep='\n')