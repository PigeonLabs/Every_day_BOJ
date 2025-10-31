import sys
from collections import Counter
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

INF = 10**8

def comp(a, b):
    if Counter(a) != Counter(b):
        return INF
    return sum(x != y for x, y in zip(a, b))

def dfs(idx):
    if idx == len(s):
        return 0
    if dp[idx] != -1:
        return dp[idx]

    res = INF
    for length in lengths:
        if idx + length > len(s):
            continue
        segment = s[idx:idx + length]
        for word in dict_by_len[length]:
            diff = comp(segment, word)
            if diff != INF:
                res = min(res, diff + dfs(idx + length))

    dp[idx] = res
    return res

s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

dict_by_len = {}
for w in words:
    dict_by_len.setdefault(len(w), []).append(w)
lengths = sorted(dict_by_len.keys())

dp = [-1] * (len(s) + 1)

ans = dfs(0)
print(ans if ans < INF else -1)