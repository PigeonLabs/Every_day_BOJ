import itertools
res = []
for _ in range(int(input())):
    res.append(max(list(sum(x)%10 for x in list(itertools.combinations(list(map(int,input().split())), 3)))))
res.reverse()
print(len(res)-res.index(max(res)))