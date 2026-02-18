import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ext = set()
count = 0

for i in range(k):
    cur = arr[i]
    if cur in ext:
        continue
    if len(ext) < n:
        ext.add(cur)
        continue
    v = None
    far = -1
    for x in ext:
        try:
            nxt = arr.index(x, i+1)
        except ValueError:
            v = x
            far = float('inf')
            break

        if nxt > far:
            far = nxt
            v = x

    ext.remove(v)
    ext.add(cur)
    count += 1

print(count)