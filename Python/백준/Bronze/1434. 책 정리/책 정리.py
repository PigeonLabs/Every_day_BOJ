n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

box = 0

for i in b:
    while i > a[box]:
        box += 1
    a[box] -= i

print(sum(a))