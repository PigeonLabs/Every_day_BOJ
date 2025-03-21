import sys
input = sys.stdin.readline

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

n, m = map(int, input().split())
roads = []

for _ in range(m):
    s, e = map(int, input().split())
    roads.append((s, e))

divisors = get_divisors(n)

for seg_size in divisors:
    region_cnt = n // seg_size
    region_num = [0] * (n + 1)

    for i in range(1, n + 1):
        region_num[i] = (i - 1) // seg_size + 1

    valid = True
    for s, e in roads:
        if region_num[s] > region_num[e]:
            valid = False
            break
    if valid:
        print(region_cnt)
        break
