import sys
input = sys.stdin.readline

s = list(input().strip())
l = len(s)

is_pal = [[0] * l for _ in range(l)]

def expand(left, right):
    while 0 <= left and right < l and s[left] == s[right]:
        is_pal[left][right] = 1
        left -= 1
        right += 1

for c in range(l):
    expand(c, c)
    expand(c, c + 1)

dp = [10**8] * l

for j in range(l):
    if is_pal[0][j]:
        dp[j] = 1
    else:
        for i in range(1, j + 1):
            if is_pal[i][j]:
                dp[j] = min(dp[j], dp[i - 1] + 1)

print(dp[-1])