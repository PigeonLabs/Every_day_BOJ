import sys, bisect
input = sys.stdin.readline

def solve(arr):
    d = []
    for x in arr:
        if not d or d[-1] <= x:
            d.append(x)
        else:
            i = bisect.bisect_right(d, x)
            d[i] = x
    return len(d)

n = int(input())
arr1 = []
arr2 = []
for _ in range(n):
    a, b = map(int, input().split())
    arr1.append([a, b])
    arr2.append([b, a])

arr1.sort()
arr2.sort()

arr1 = [x[1] for x in arr1]
arr2 = [x[1] for x in arr2]

print(min(n-solve(arr1), n-solve(arr2)))