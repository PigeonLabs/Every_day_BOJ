import sys
input = sys.stdin.readline

MOD = 1000003

def mul(a, b):
    res = [[0] * size for _ in range(size)]

    for i in range(size):
        ai = a[i]
        ri = res[i]
        for k in range(size):
            if ai[k] == 0:
                continue
            aik = ai[k]
            bk = b[k]
            for j in range(size):
                if bk[j]:
                    ri[j] = (ri[j] + aik * bk[j]) % MOD

    return res

def mat_pow(mat, exp):
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1

    while exp:
        if exp & 1:
            res = mul(res, mat)
        mat = mul(mat, mat)
        exp >>= 1

    return res

n, s, e, t = map(int, input().split())
board = [input().strip() for _ in range(n)]

size = n * 5
mat = [[0] * size for _ in range(size)]

for i in range(n):
    base = i * 5
    for k in range(1, 5):
        mat[base + k][base + k - 1] = 1

for i in range(n):
    for j in range(n):
        d = int(board[i][j])
        if d == 0:
            continue
        if d == 1:
            mat[i * 5][j * 5] += 1
        else:
            mat[i * 5][j * 5 + d - 1] += 1

ans = mat_pow(mat, t)
print(ans[(s - 1) * 5][(e - 1) * 5] % MOD)