def leaf(year):
    year = int("".join(year))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False

def years(year):
    res = []
    def rec(i, cur):
        if i == len(year):
            if cur != "0000":
                res.append(cur.zfill(len(year)))
            return
        if year[i] == 'X':
            for d in "0123456789":
                rec(i+1, cur+d)
        else:
            rec(i+1, cur+year[i])
    rec(0, "")
    return res

def months(month):
    if month[0] != 'X' and month[1] != 'X':
        mon = int("".join(month))
        if 1 <= mon <= 12:
            return [str(mon).zfill(2)]
        return []
    elif month[0] == 'X' and month[1] == 'X':
        return [str(x).zfill(2) for x in range(1, 13)]
    elif month[0] == 'X':
        return [(p + month[1]).zfill(2) for p in ['0', '1'] if 1 <= int(p + month[1]) <= 12]
    elif month[1] == 'X':
        return [month[0] + str(d) for d in range(10) if 1 <= int(month[0] + str(d)) <= 12]
    return []

def days(day, limit):
    if day[0] != 'X' and day[1] != 'X':
        return ["".join(day).zfill(2)] if 1 <= int("".join(day)) <= limit else []
    elif day[0] == 'X' and day[1] == 'X':
        return [str(x).zfill(2) for x in range(1, limit+1)]
    elif day[0] == 'X':
        return [(str(x) + day[1]) for x in range(4) if 1 <= int(str(x)+day[1]) <= limit]
    elif day[1] == 'X':
        return [(day[0] + str(x)) for x in range(10) if 1 <= int(day[0]+str(x)) <= limit]

def process_an(pattern, mod2):
    n = len(pattern)
    dp = [[0] * 19 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        coeff = mod2[i]
        ch = pattern[i]
        for r in range(19):
            if dp[i][r] == 0:
                continue
            if ch == 'X':
                for d in range(10):
                    new_r = (r + coeff * d) % 19
                    dp[i+1][new_r] += dp[i][r]
            else:
                d = int(ch)
                new_r = (r + coeff * d) % 19
                dp[i+1][new_r] += dp[i][r]
    mod2l = dp[n]
    valid_zero = True
    for ch in pattern:
        if ch != 'X' and ch != '0':
            valid_zero = False
            break
    if valid_zero:
        mod2l[0] -= 1
    return mod2l

l = list(input())
res = 0;
day = l[0:2]
month = l[2:4]
year = l[4:8]
an = l[8:18]
cn = l[18]

d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
ld = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if cn=='X':
    yr,lyr = 0,0
    for i in years(year):
        if leaf(i):
            lyr += 1
        else:
            yr += 1
    ndl,dl = 0,0
    for m in list(map(int,months(month))):
        ndl += len(days(day,d[m]))
        dl += len(days(day,ld[m]))
    res = (lyr*dl + yr*ndl) * 10**an.count('X')
    print(res)
else:
    mod1 = [10, 9, 8, 7, 6, 5, 4, 3]
    mod1l = [0]*19
    mod2 = [2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    mod2l = process_an(an,mod2)

    freq_nonfeb = [0] * 19
    freq_feb_noleap = [0] * 19
    freq_feb_leap = [0] * 19
    
    for j in months(month):
        m = int(j)
        if m == 2:
            for k in days(day, d[m]):
                r_dm = (int(k[0]) * mod1[0] + int(k[1]) * mod1[1] +
                        int(j[0]) * mod1[2] + int(j[1]) * mod1[3]) % 19
                freq_feb_noleap[r_dm] += 1
            for k in days(day, ld[m]):
                r_dm = (int(k[0]) * mod1[0] + int(k[1]) * mod1[1] +
                        int(j[0]) * mod1[2] + int(j[1]) * mod1[3]) % 19
                freq_feb_leap[r_dm] += 1
        else:
            for k in days(day, d[m]):
                r_dm = (int(k[0]) * mod1[0] + int(k[1]) * mod1[1] +
                        int(j[0]) * mod1[2] + int(j[1]) * mod1[3]) % 19
                freq_nonfeb[r_dm] += 1

    year_coeff = mod1[4:]
    years_list = years(year)
    for y in years_list:
        r_year = sum(int(y[i]) * year_coeff[i] for i in range(4)) % 19
        for r_dm, cnt in enumerate(freq_nonfeb):
            total_r = (r_dm + r_year) % 19
            mod1l[total_r] += cnt
        if leaf(y):
            for r_dm, cnt in enumerate(freq_feb_leap):
                total_r = (r_dm + r_year) % 19
                mod1l[total_r] += cnt
        else:
            for r_dm, cnt in enumerate(freq_feb_noleap):
                total_r = (r_dm + r_year) % 19
                mod1l[total_r] += cnt
                
    for m1 in [int(cn), 19 - int(cn)]:
        m2 = 0
        for i in range(19):
            res += mod1l[m1] * mod2l[m2]
            m1 += 1
            if m1 == 19:
                m1 = 0
            m2 -= 1
    print(res)