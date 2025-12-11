nums = {
    0: {0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14},
    1: {2, 5, 8, 11, 14},
    2: {0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14},
    3: {0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14},
    4: {0, 2, 3, 5, 6, 7, 8, 11, 14},
    5: {0, 1, 2, 3, 6, 7, 8, 11, 12, 13, 14},
    6: {0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14},
    7: {0, 1, 2, 5, 8, 11, 14},
    8: {0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14},
    9: {0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14}
}

def timenum(n):
    res = set()
    cand = []
    for y in range(5):
        for x in range(3):
            if arr[y][x+4*n] == '#':
                res.add(y*3+x)
    for i in range(10):
        if res <= nums[i]:
            cand.append(i)
    return cand

arr = [list(input()) for _ in range(5)]
t = []
for i in range(4):
    t.append(timenum(i))
h = [a*10+b for a in t[0] for b in t[1] if a*10+b<24]
m = [a*10+b for a in t[2] for b in t[3] if a*10+b<60]
print(f"{h[0]:02}:{m[0]:02}")