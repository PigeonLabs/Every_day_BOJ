import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dv = 1000000007

n,m,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
tree = [0] * (n * 4)

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = (init(node*2, start, mid) * init(node*2+1, mid+1, end)) % dv
    return tree[node]

#업데이트
def update_val(node, start, end, pos, val):    
    if pos > end or pos < start:
        return
    if start == end:
        tree[node] = val
        return
    
    mid = (start + end) // 2
    update_val(node*2, start, mid, pos, val)
    update_val(node*2+1, mid+1, end, pos, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % dv

#구간곱
def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return (query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right)) % dv

init(1, 0, n-1)
for _ in range(m + k):
    a,b,c = map(int, input().split())
    if a == 1:
        update_val(1, 0, n-1, b-1, c)
    else:
        print(query(1, 0, n-1, b-1, c-1))