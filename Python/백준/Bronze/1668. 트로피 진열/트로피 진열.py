def solve(t):
    cnt = 0
    mx = 0
    for i in t:
        if i > mx:
            mx = i
            cnt += 1
    return cnt

n = int(input())
arr = [int(input()) for _ in range(n)]

print(solve(arr))
print(solve(arr[::-1]))