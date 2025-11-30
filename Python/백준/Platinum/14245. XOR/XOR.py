import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

tree = [0] * (n * 4)

#구간업데이트
def update_range(node, start, end, left, right, data):
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] ^= data
        return
    
    mid = (start + end) // 2
    update_range(node*2, start, mid, left, right, data)
    update_range(node*2+1, mid+1, end, left, right, data)

#구간합
def query(node, start, end, pos):    
    if start == end:
        return tree[node]
    
    mid = (start + end) // 2
    if pos <= mid:
        return query(node*2, start, mid, pos) ^ tree[node]
    else:
        return query(node*2+1, mid+1, end, pos) ^ tree[node]

for _ in range(m):
    t = list(map(int, input().split()))
    if t[0]==1:
        update_range(1, 0, n-1, t[1], t[2], t[3])
    else:
        print(arr[t[1]] ^ query(1, 0, n-1, t[1]))