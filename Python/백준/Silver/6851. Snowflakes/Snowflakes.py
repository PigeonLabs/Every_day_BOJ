n = int(input())
s = set()
for _ in range(n):
    a = tuple(sorted(list(map(int, input().split()))))
    if a not in s:
        s.add(a)
    else:
        print("Twin snowflakes found.")
        exit()
print("No two snowflakes are alike.")