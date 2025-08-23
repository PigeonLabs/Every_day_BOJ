t = int(input())
n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

npref = [0] * (n + 1)
mpref = [0] * (m + 1)
for i in range(n):
    npref[i+1] = npref[i] + narr[i]
for i in range(m):
    mpref[i+1] = mpref[i] + marr[i]

ns,ms = set(),set()
nd,md = {},{}
for i in range(n):
    for j in range(i, n):
        x = npref[j+1] - npref[i]
        ns.add(x)
        nd[x] = nd.get(x, 0) + 1
for i in range(m):
    for j in range(i, m):
        x = mpref[j+1] - mpref[i]
        ms.add(x)
        md[x] = md.get(x, 0) + 1

res = 0
for i in ns:
    if t - i in ms:
        res += nd[i]*md[t - i]

print(res)