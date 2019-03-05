def find_tree(node):
    global cnt
    if node != 0:
        cnt+=1
        find_tree(tree[node][0])
        find_tree(tree[node][1])
    return cnt

import sys
sys.stdin = open("서브_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E + 2)]

    cnt = 0
    for i in range(E):
        n1 = temp[i*2]
        n2 = temp[i*2 + 1]
        if not tree[n1][0]:     #값이 비어있으면 왼쪽 값을 넣는다
            tree[n1][0] = n2
        else:   #왼쪽값이 채워져 있으면 오른쪽 값을 넣는다
            tree[n1][1] = n2
        tree[n2][2] = n1    #부모값 채우기

    print("#{} {}".format(tc, find_tree(N)))