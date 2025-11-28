import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
tree = [0] * (n * 4)
lazy = [0] * (n * 4)

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

#Lazy값 전파(단일)
def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

#구간업데이트
def update_range(node, start, end, left, right, diff):
    propagate(node, start, end)
    
    if left > end or right < start:
        return
    
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    
    mid = (start + end) // 2
    update_range(node*2, start, mid, left, right, diff)
    update_range(node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

#구간합
def query(node, start, end, left, right):
    propagate(node, start, end)
    
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

init(1, 0, n-1)
for _ in range(m + k):
    o, *cmd = map(int, input().split())
    if o == 1:
        b, c, d = cmd
        update_range(1, 0, n-1, b-1, c-1, d)
    else:
        b, c = cmd
        print(query(1, 0, n-1, b-1, c-1))