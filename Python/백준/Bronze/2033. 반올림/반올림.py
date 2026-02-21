def baekjoon_round(N):
    compare_num = 10
    while N >= compare_num:
        if N % compare_num >= compare_num // 2:
            N += compare_num
        N -= (N % compare_num)
        compare_num *= 10
    return N

N = int(input())
print(baekjoon_round(N))