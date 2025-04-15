n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
if n==2:
    print("1 1")
    exit()
res = [0,0]
res[1] = (arr[0][1] + arr[1][2] - arr[0][2])//2
res[0] = arr[0][1] - res[1]
res += [x - res[0] for x in arr[0]][2:]
print(*res)