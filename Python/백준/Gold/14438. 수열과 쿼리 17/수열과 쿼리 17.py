import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
arr = [0] * (4 * n)

def init(start, end, node):
    if start == end:
        arr[node] = a[start]
        return arr[node]
    mid = (start + end) // 2
    arr[node] = min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1))
    return arr[node]

def update(start, end, node, idx, val):
    if idx < start or idx > end:
        return arr[node]
    if start == end:
        arr[node] = val
        return arr[node]
    mid = (start + end) // 2
    arr[node] = min(update(start, mid, node * 2, idx, val),
                    update(mid + 1, end, node * 2 + 1, idx, val))
    return arr[node]

def query(start, end, node, left, right):
    if right < start or end < left:
        return float('inf')
    if left <= start and end <= right:
        return arr[node]
    mid = (start + end) // 2
    return min(query(start, mid, node * 2, left, right),
               query(mid + 1, end, node * 2 + 1, left, right))

init(0, n - 1, 1)

m = int(input())
for _ in range(m):
    x, i, j = map(int, input().split())
    if x == 1:
        update(0, n - 1, 1, i - 1, j)
    else:
        print(query(0, n - 1, 1, i - 1, j - 1))