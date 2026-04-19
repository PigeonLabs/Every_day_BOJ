import sys
input = sys.stdin.readline

def insert(path):
    cur = trie
    for food in path:
        if food not in cur:
            cur[food] = {}
        cur = cur[food]

def dfs(node, depth):
    for key in sorted(node):
        ans.append("--" * depth + key)
        dfs(node[key], depth + 1)

n = int(input())
trie = {}

for _ in range(n):
    data = input().split()
    insert(data[1:])

ans = []
dfs(trie, 0)
print("\n".join(ans))