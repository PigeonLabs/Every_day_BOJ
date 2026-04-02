import itertools

n = int(input())
c = list(str(n))
for i in sorted([int(''.join(p)) for p in itertools.permutations(c, len(c))]):
    if i > n:
        print(i)
        exit()
print(0)