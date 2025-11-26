import sys,math
input = sys.stdin.readline

def div(n):
    d = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(list(d))

d,m = map(int, input().split())
lcm = math.lcm(*map(int, input().split()))
gcd = math.gcd(*map(int, input().split()))

res = 0
for i in div(gcd):
    if i%lcm == 0:
        res += 1
print(res)