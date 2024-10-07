import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = zip(*[map(int, input().split()) for _ in range(n)])

def result(A,B,C,D):
    v = dict()

    for i in range(n):
        for j in range(n):
            v[C[i]+D[j]] = v.get(C[i]+D[j], 0) + 1
    
    res = 0
    for i in A:
        for j in B:
            if -(i+j) in v:
                res += v[-i-j]

    return res

print(result(A,B,C,D))