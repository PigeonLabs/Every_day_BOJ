N = int(input())
info = []
array = [[-1] * 1001 for _ in range(1001)]

max_index_height, max_index_width = 0, 0
for k in range(N):
    x1, y1, w, h = list(map(int, input().split()))

    if max_index_height < y1 + h:
        max_index_height = y1 + h

    for a in range(y1, y1 + h):
        array[a][x1:(x1 + w)] = [k] * w

for k in range(N):
    count = 0
    for i in range(max_index_height):
        count += array[i].count(k)

    print(count)