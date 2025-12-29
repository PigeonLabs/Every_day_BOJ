time = list(map(int,input().split(':')))
h = 0
x = 0
for i in time:
    if 0 < i < 13:
        h += 1
    if 59 < i <100:
        x -= 1
print(0 if x<0 else h*2)