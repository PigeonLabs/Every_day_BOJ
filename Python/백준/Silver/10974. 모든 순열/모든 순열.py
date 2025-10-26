from itertools import permutations
print(*[" ".join(map(str,p))for p in permutations(range(1,int(input())+1))],sep="\n")