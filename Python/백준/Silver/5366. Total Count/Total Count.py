import sys
input = sys.stdin.readline

fighters = {}
while True:
    x = input().strip()
    if x == "0":
        break
    else:
        fighters[x] = fighters.get(x, 0) + 1

res = 0
for fighter,count in fighters.items():
    print(f"{fighter}: {count}")
    res += count
print("Grand Total:", res)