s = input()
p = input()

m, n = len(s), len(p)

lcp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if p[i] == s[j]:
            lcp[i][j] = 1 + lcp[i+1][j+1]

res = 0
i = 0
while i < n:
    i += max(lcp[i])
    res += 1
print(res)
