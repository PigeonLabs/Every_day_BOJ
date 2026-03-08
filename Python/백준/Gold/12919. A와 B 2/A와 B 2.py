s = input()
t = input()

def solve(word):
    if len(word) == len(s):
        return 1 if word == s else 0
    ans = 0
    if word[0] == 'B':
        ans |= solve(word[1:][::-1])
    if word[-1] == 'A':
        ans |= solve(word[:-1])
    return ans

print(solve(t))