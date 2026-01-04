import sys

def stoneFunc(n):
    if n %2 == 0:
        return n //2 
    else :
        return (n*3)+1

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    max = 1
    while n != 1 :
        if max < n : max = n
        n = stoneFunc(n)
    
    print(max)