import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m = map(int, input().split())
tree = [0] * (n * 4)
lazy = [0] * (n * 4)

#Lazy값 전파(단일)
def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0

#구간업데이트
def update_range(node, start, end, left, right):
    propagate(node, start, end)
    
    if left > end or right < start:
        return
    
    if left <= start and end <= right:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        return
    
    mid = (start + end) // 2
    update_range(node*2, start, mid, left, right)
    update_range(node*2+1, mid+1, end, left, right)
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

for _ in range(m):
    o,s,t = map(int, input().split())
    if o:
        print(query(1, 0, n-1, s-1, t-1))        
    else:
        update_range(1, 0, n-1, s-1, t-1)
        