n = int(input())

left = 1
right = n
while left < right:
    mid = (left + right) // 2
    if n < mid * mid:
        right = mid
    else:
        left = mid + 1
print(left - 1)