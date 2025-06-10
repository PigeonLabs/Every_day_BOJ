n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx ** 2 + dy ** 2

    if d2 == 0:
        print(-1 if r1 == r2 else 0)
    elif d2 > (r1 + r2) ** 2 or d2 < (r1 - r2) ** 2:
        print(0)
    elif d2 == (r1 + r2) ** 2 or d2 == (r1 - r2) ** 2:
        print(1)
    else:
        print(2)