n, k = map(int, input().split())
res = [0 for _ in range(k+1)]
for i in range(n):
    w, v = map(int, input().split())
    for t in range(k, w-1, -1):
        res[t] = max(res[t], res[t-w] + v)
print(res[-1])