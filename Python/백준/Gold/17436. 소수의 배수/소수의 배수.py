from math import gcd
from functools import reduce
from itertools import combinations

def lcm_two(a,b):
    return a // gcd(a, b) * b

def lcm_list(nums):
    return reduce(lcm_two, nums)

n, m = map(int, input().split())
l = list(map(int, input().split()))

res = 0
for i in range(1, n + 1):
    for comb in combinations(l, i):
        current_lcm = lcm_list(comb)
        count = m // current_lcm
        if i % 2 == 1:
            res += count
        else:
            res -= count

print(res)
