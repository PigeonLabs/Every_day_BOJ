import sys
input = sys.stdin.readline

while True:
    try:
        n, *a = map(int, input().split())
        s = set()
        for i in range(n-1):
            s.add(abs(a[i] - a[i+1]))
        if n == 1:
            print("Jolly")
        elif len(s) == n-1 and min(s) == 1 and max(s) == n-1:
            print("Jolly")
        else:
            print("Not jolly")
    except :
        break