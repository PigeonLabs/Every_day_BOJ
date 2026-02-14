import sys
input = sys.stdin.readline

P, W = map(int, input().split())
text = input().rstrip()

groups = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
key_map = {}

for key_idx, chars in enumerate(groups):
    for press_cnt, char in enumerate(chars, 1):
        key_map[char] = (key_idx, press_cnt)

total_time = 0
prev_key = -1

for char in text:
    if char == ' ':
        total_time += P
        prev_key = -1
    elif char in key_map:
        key_idx, press_cnt = key_map[char]
        
        if key_idx == prev_key:
            total_time += W
        
        total_time += press_cnt * P
        prev_key = key_idx

print(total_time)