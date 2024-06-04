from itertools import combinations
rl = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
l = [11, 56, 176, 386, 638, 848, 968, 1013, 1023]

n = int(input())
if n > 1023:
    print(-1)
elif n < 11:
    print(n-1)
elif n==1023:
    print(9876543210)
else:
    i = 0
    while l[i] <= n:
        i += 1
    int_list = [int("".join(map(str, t))) for t in combinations(rl, i+1)]
    int_list.sort()
    print(int_list[n - l[i-1]])