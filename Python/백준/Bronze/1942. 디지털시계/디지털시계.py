import datetime
from datetime import timedelta

for i in range(3):
    line = input().split()
    if not line: break
    start, end = line

    stH, stM, stS = map(int, start.split(":"))
    edH, edM, edS = map(int, end.split(":"))

    stime = datetime.datetime(2021, 1, 1, stH, stM, stS)
    etime = datetime.datetime(2021, 1, 1, edH, edM, edS)

    if stime > etime:
        etime += timedelta(days=1)

    cnt = 0
    tmp_time_obj = stime
    
    while True:
        tmp_time_str = tmp_time_obj.strftime('%H%M%S')
        if int(tmp_time_str) % 3 == 0:
            cnt += 1
        
        if tmp_time_obj == etime:
            break
            
        tmp_time_obj += timedelta(seconds=1)

    print(cnt)