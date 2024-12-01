from math import comb
import itertools
res = 0
a = int(input())/100
b = int(input())/100
for ga,gb in itertools.product([0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18], repeat=2):
    res += comb(18, ga) * (a**ga)*((1-a)**(18-ga)) * comb(18, gb) * (b**gb)*((1-b)**(18-gb))
print(1 - res)