import sys
input = sys.stdin.readline

a,b,k = map(int, input().split())
arr = {}
res = 0
for n in range(a,b+1):
    if n not in arr:
        s = {n}
        l = [n]
        x = sum(int(c)**k for c in str(l[-1]))
        while True:
            if x in s:
                t = l.index(x)
                mn = min(l[t:])
                for i in range(t):
                    arr[l[i]] = min(min(l[i:t]), mn)
                for i in l[t:]:
                    arr[i] = mn
                break
            if x in arr:
                r = arr[x]
                for v in reversed(l):
                    if v < r:
                        r = v
                    arr[v] = r
                break

            s.add(x)
            l.append(x)
            x = sum(int(c)**k for c in str(l[-1]))
    res += arr[n]

print(res)