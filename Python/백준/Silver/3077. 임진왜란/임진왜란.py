import sys,itertools
input = sys.stdin.readline

n = int(input())
ans = list(map(str,input().split()))
d = {word: i for i, word in enumerate(map(str,input().split()))}
res = 0
for i in itertools.combinations(ans, 2):
    if d[i[0]] < d[i[1]]:
        res += 1
print(f"{res}/{str(n*(n-1)//2)}")