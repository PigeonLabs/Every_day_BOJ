import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    k = int(input())
    C = list(map(int, input().split()))
    res = set()
    for a in A:
        for b in B:
            for c in C:
                r = a + b + c
                if set(str(r)) <= set('58'):
                    res.add(r)
    print(len(res))