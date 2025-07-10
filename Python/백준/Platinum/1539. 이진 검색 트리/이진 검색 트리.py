import sys,random
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, key, depth):
        self.key = key
        self.prio = random.random()
        self.depth = depth
        self.left = None
        self.right = None

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def treap_insert(root, node):
    if not root:
        return node
    if node.key < root.key:
        root.left = treap_insert(root.left, node)
        if root.left.prio < root.prio:
            root = rotate_right(root)
    else:
        root.right = treap_insert(root.right, node)
        if root.right.prio < root.prio:
            root = rotate_left(root)
    return root

def find_neighbors(root, x):
    pred = succ = None
    cur = root
    while cur:
        if x < cur.key:
            succ = cur
            cur = cur.left
        else:
            if cur.key < x:
                pred = cur
            cur = cur.right
    return pred, succ

n = int(input())
root = None
total = 0

for _ in range(n):
    x = int(input())
    pred, succ = find_neighbors(root, x)
    left_depth  = pred.depth if pred else 0
    right_depth = succ.depth if succ else 0
    curr_depth = max(left_depth, right_depth) + 1
    total += curr_depth
    node = Node(x, curr_depth)
    root = treap_insert(root, node)
    
print(total)