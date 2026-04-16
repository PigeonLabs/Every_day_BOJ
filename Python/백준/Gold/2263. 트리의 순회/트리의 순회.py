import sys
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

ans = []
stack = [(0, n - 1, 0, n - 1)]

while stack:
    il, ir, pl, pr = stack.pop()
    if il > ir:
        continue

    root = postorder[pr]
    ans.append(root)

    mid = pos[root]
    left = mid - il
    right = ir - mid

    if right:
        stack.append((mid + 1, ir, pl + left, pr - 1))
    if left:
        stack.append((il, mid - 1, pl, pl + left - 1))

print(*ans)