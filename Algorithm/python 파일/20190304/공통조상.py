def preorder(node):
    global cnt
    if node:
        cnt+=1
        preorder(tree[node][0])
        preorder(tree[node][1])

def find_P(n1, n2):
    p1 = []
    start = tree[n1][2]
    while start:
        p1.append(start)
        start = tree[start][2]
    start = tree[n2][2]
    while start:
        if start in p1:
            return start
        start = tree[start][2]

import sys
sys.stdin = open('공조_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]

    cnt = 0

    for i in range(0, len(temp), 2):
        tree[temp[i + 1]][2] = temp[i]
    for i in range(1, V + 1):
        P = tree[i][2]
        if P:
            if tree[P][0]:
                tree[P][1] = i
            else:
                tree[P][0] = i
    sub_tree = find_P(n1, n2)
    preorder(sub_tree)
    print('#{} {} {}'.format(tc, sub_tree, cnt))
