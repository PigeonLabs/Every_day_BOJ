import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
p = []
p.append([x1,y1])
p.append([x2,y2])
p.append([x3,y3])
p.append([x4,y4])

def ccw(p1,p2,p3):
    t = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
    return 1 if t>0 else -1 if t<0 else 0

def cross(p1,p2,p3,p4):
    tres,res = 0,0

    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p134 = ccw(p1, p3, p4)
    p234 = ccw(p2, p3, p4)

    if p123*p124 == 0 and p134*p234 == 0:
        tres = 1
        if min(p1[0], p2[0])<=max(p3[0],p4[0]) and min(p3[0],p4[0])<=max(p1[0],p2[0]) and min(p1[1],p2[1])<=max(p3[1],p4[1]) and min(p3[1],p4[1])<=max(p1[1],p2[1]):
            res = 1
    if p123*p124 <= 0 and p134*p234 <= 0:
        if not tres:
            res = 1
        
    return res
    
print(cross(p[0],p[1],p[2],p[3]))