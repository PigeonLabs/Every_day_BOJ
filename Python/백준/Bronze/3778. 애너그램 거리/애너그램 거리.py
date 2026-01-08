import sys
input = sys.stdin.readline

N = int(input())

base_char_code = ord('a')

for n in range(1, N + 1):
    A = input().rstrip()
    B = input().rstrip()

    alphabat_count = [0] * 26

    for a in A:
        i = ord(a) - base_char_code
        
        alphabat_count[i] += 1
    
    for b in B:
        j = ord(b) - base_char_code

        alphabat_count[j] -= 1

    distance = sum([k if 0 < k else -k for k in alphabat_count if k != 0])

    print(f'Case #{n}: {distance}')