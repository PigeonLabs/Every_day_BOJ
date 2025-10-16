from collections import Counter

res = 0
nums = []
for i in range(10):
    n = int(input())
    nums.append(n)
    res += n
print(res//10)
print(Counter(nums).most_common(1)[0][0])