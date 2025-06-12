def solve(i,j,res):
    if len(res) == 6:
        s.add(tuple(res))
        return
    for di,dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        if 0 <= i+di < 5 and 0 <= j+dj < 5:
            solve(i+di, j+dj, res + [l[i+di][j+dj]])

l = []
for _ in range(5):
    l.append(list(map(int, input().split())))

s = set()
for i in range(5):
    for j in range(5):
        solve(i, j, [l[i][j]])

print(len(s))