import sys
input = sys.stdin.readline

def seg(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(seg(node*2, start, mid), seg(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if right < start or left > end:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

n,m = map(int, input().split())
arr = []
tree = [0] * (4*n)
for _ in range(n):
    arr.append(int(input()))
seg(1, 0, n-1)
for _ in range(m):
    a,b = map(int,input().split())
    print(query(1, 0, n-1, a-1, b-1))