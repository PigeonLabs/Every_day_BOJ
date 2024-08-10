import sys

for _ in range(int(sys.stdin.readline())):
    co, vec, check = [], [], 0
    
    for i in range(4):
        co.append(list(map(int, sys.stdin.readline().split())))
        
    for i in range(4):
        for j in range(i+1, 4):
            vec.append([co[j][0] - co[i][0], co[j][1] - co[i][1]])
            
    for i in range(6):
        for j in range(i+1, 6):
            if vec[i][0]*vec[j][0] + vec[i][1]*vec[j][1] == 0:
                check += 1
                
    if check == 5:
        print(1)
    else:
        print(0)