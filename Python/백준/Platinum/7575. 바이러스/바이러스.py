import sys
input = sys.stdin.readline

def compute_lps(p, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length == 0:
            lps[i] = 0
            i += 1
        else:
            length = lps[length - 1]

def kmp(t, p):
    lt, lp = len(t), len(p)
    lps_arr = [0] * lp
    compute_lps(p, lps_arr)
    i, j = 0, 0
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == lp:
                return True
        else:
            if j != 0:
                j = lps_arr[j - 1]
            else:
                i += 1
    return False

n, k = map(int, input().split())
l = [None] * n
lr = [None] * n

for idx in range(n):
    input()
    l[idx] = list(map(int, input().split()))
    lr[idx] = l[idx][::-1]

for start in range(len(l[0]) - k + 1):
    pattern = l[0][start:start+k]
    valid = True
    for j in range(1, n):
        if not (kmp(l[j], pattern) or kmp(lr[j], pattern)):
            valid = False
            break
    if valid:
        print("YES")
        sys.exit(0)
print("NO")
