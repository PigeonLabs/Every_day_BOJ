import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n<3:
    if n==2 and arr[0]==arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    if arr[0]==arr[1]:
        if len(set(arr))==1:
            print(arr[0])
        else:
            print("B")
    else:
        if arr[1]==arr[2]:
            if len(set(arr[1:]))==1:
                print(arr[1])
            else:
                print("B")
        else:
            if (arr[2]-arr[1])%(arr[1]-arr[0])!=0:
                print("B")
            else:
                a = (arr[2] - arr[1]) // (arr[1] - arr[0])
                b = arr[1] - arr[0]*a
                for i in range(1,n):
                    if arr[i] != arr[i-1]*a+b:
                        print("B")
                        exit()
                print(arr[-1]*a+b)
