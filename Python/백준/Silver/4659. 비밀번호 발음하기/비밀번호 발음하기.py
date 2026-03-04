import sys
input = sys.stdin.readline

def solve(s):
    recent = ''
    vowel = 0
    v,c = 0,0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            vowel += 1
            v += 1
            c = 0
        else:
            c += 1
            v = 0
        if recent == s[i] and s[i] not in 'eo':
            return False
        if v == 3 or c == 3:
            return False
        recent = s[i]
    if vowel == 0:
        return False
    return True

while True:
    s = input().rstrip()
    if s == 'end':
        break
    if solve(s):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")