import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    val = a*b
    a = list(str(a))
    b = list(str(b))
    length = min(len(a),len(b))
    res = ""
    if length<len(a):
        res = "".join(a[:len(a)-length])
        a = a[len(a)-length:]
    if length<len(b):
        res = "".join(b[:len(b)-length])
        b = b[len(b)-length:]
    for i in range(len(a)):
        res += str(int(a[i]) * int(b[i]))
    if (val==int(res)):
        print(1)
    else:
        print(0)