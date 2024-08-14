import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ans = "NO"
    n,m,w = map(int,input().split())
    graph = []
    hole = []
    for _ in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))
        hole.append(s)

    for i in hole:
        res = [10**8 for _ in range(n+1)]
        res[i] = 0
        for i in range(n+1):
            for a,b,c in graph:
                if res[a] != 10**8 and res[b] > res[a]+c:
                    res[b] = res[a]+c
                    if i==n:
                        ans = "YES"
                        break
            if ans == "YES":
                break
        if ans == "YES":
            break
    
    print(ans)