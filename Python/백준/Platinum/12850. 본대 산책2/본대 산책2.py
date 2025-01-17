import sys
sys.setrecursionlimit(10**9)

mod = 1000000007

def multi(a, b):
    n = 8
    arr = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for k in range(n):
                arr[row][col] = (arr[row][col] + a[row][k] * b[k][col]) % mod
    return arr

def pow(arr, r):
    if r == 1:
        return arr
    half = pow(arr, r // 2)
    halfsq = multi(half, half)
    if r % 2 == 0:
        return halfsq
    else:
        return multi(halfsq, arr)

matrix = [
    [0,1,1,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,1,1,0,0],
    [1,1,1,0,0,1,0,0],
    [0,0,1,0,0,1,1,0],
    [0,0,1,1,1,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,0,1,1,0]
]

n = int(input())
print(pow(matrix, n)[1][1] % mod)