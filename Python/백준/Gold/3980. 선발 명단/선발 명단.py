import sys
input = sys.stdin.readline

c = int(input())

def backtracking(cnt, sum):
    global result
    if cnt == 11:
        result = max(result, sum)
        return
    for i in range(11):
        if members[i] or not powers[cnt][i]:
            continue
        members[i] = 1
        backtracking(cnt + 1, sum + powers[cnt][i])
        members[i] = 0

for _ in range(c):
    powers = [list(map(int, input().split())) for _ in range(11)]
    members = [0 for _ in range(11)]
    result = 0
    backtracking(0, 0)
    print(result)