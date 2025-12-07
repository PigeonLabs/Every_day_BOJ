import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
arr = list(map(int, input().split()))
tree = [0] * (n * 4)

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], start)
        return tree[node]
    
    mid = (start + end) // 2
    lval = init(node*2, start, mid)
    rval = init(node*2+1, mid+1, end)
    if lval[0] <= rval[0]:
        tree[node] = lval
    else:
        tree[node] = rval
    return tree[node]

def update_range(node, start, end, pos, val): 
    if pos < start or end < pos:
        return
    
    if start == end and start == pos:
        tree[node] = (val, pos)
        return
    
    mid = (start + end) // 2
    update_range(node*2, start, mid, pos, val)
    update_range(node*2+1, mid+1, end, pos, val)
    if tree[node*2][0] <= tree[node*2+1][0]:
        tree[node] = tree[node*2]
    else:
        tree[node] = tree[node*2+1]

def query(node, start, end, left, right):
    if left > end or right < start:
        return (float('inf'), -1)
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    lres = query(node*2, start, mid, left, right)
    rres = query(node*2+1, mid+1, end, left, right)
    if lres[0] <= rres[0]:
        return lres
    else:
        return rres
    
init(1, 0, n-1)
for _ in range(m:=int(input())):
    a,b,c = map(int, input().split())
    if a == 1:
        update_range(1, 0, n-1, b-1, c)
    else:
        print(query(1, 0, n-1, b-1, c-1)[1]+1)