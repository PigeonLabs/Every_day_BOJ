def ccw(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())
if ccw(x1, y1, x2, y2, x3, y3) > 0:
    print(1)
elif ccw(x1, y1, x2, y2, x3, y3) < 0:
    print(-1)
else:
    print(0)