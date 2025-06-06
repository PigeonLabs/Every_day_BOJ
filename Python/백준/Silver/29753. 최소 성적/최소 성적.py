import sys
input = sys.stdin.readline

grade_to_gpa = {
    "A+": 450,
    "A0": 400,
    "B+": 350,
    "B0": 300,
    "C+": 250,
    "C0": 200,
    "D+": 150,
    "D0": 100,
    "F":  000
}

s = input().split()
n = int(s[0])
X_str = s[1]
a, b = X_str.split('.')
x = int(a) * 100 + int(b)

tc = 0
tg = 0
for i in range(n-1):
    s = input().split()
    c = int(s[0])
    g = s[1]
    tc += c
    tg += c*grade_to_gpa[g]
c = int(input())
tc += c


for grade, score in sorted(grade_to_gpa.items(), key=lambda x: x[1]):
    #print(int((c * score + tg) / tc) , x)
    if (c * score + tg) // tc > x:
        print(grade)
        exit()
print("impossible")