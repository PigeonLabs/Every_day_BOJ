import sys
input = sys.stdin.readline

def prefixlst(lst):
    result = [lst]
    while len(lst) > 1:
        new_lst = [lst[i] + lst[i+1] for i in range(0, len(lst) - 1, 2)]
        if len(lst) % 2 == 1:
            new_lst.append(lst[-1])
        result.append(new_lst)
        lst = new_lst
    return result

def change(lc,nm,l):
    t = nm - l[0][lc]
    for i in range(len(l)):
        l[i][lc] += t
        lc //= 2

def printsum(a, b):
    layer = 0
    res = 0
    while a <= b:
        if a % 2 == 1:
            res += l[layer][a]
            a += 1
        if b % 2 == 0:
            res += l[layer][b]
            b -= 1
        a //= 2
        b //= 2
        layer += 1
    return res

n,m,k = map(int,input().split())
l = []
for _ in range(n):
    l.append(int(input()))
l = prefixlst(l)
for _ in range(m+k):
    command,a,b = map(int,input().split())
    if command==1:
        change(a-1,b,l)
    else:
        print(printsum(a-1,b-1))