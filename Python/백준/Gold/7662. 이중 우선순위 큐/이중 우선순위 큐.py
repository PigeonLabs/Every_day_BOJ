import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    minheap = []
    maxheap = []
    num = dict()
    for _ in range(int(input())):
        t, n = map(str,input().split())
        n = int(n)
        if t=="I":
            heapq.heappush(minheap, n)
            heapq.heappush(maxheap, -n)
            if n in num:
                num[n] += 1
            else:
                num[n] = 1
        elif t=="D" and n==1 and len(num)!=0:
            while True:
                a = -heapq.heappop(maxheap)
                if a in num:
                    break
            num[a] -= 1
            if num[a] == 0:
                del num[a]
        elif t=="D" and n==-1 and len(num)!=0:
            while True:
                a = heapq.heappop(minheap)
                if a in num:
                    break
            num[a] -= 1
            if num[a] == 0:
                del num[a]
    if len(num)==0:
        print("EMPTY")
    else:
        while True:
            mn = heapq.heappop(minheap)
            if mn in num:
                break
        while True:
            mx = -heapq.heappop(maxheap)
            if mx in num:
                break
        print(mx,mn)