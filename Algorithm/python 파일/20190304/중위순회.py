def inorder(node):
    if node != 0:
        inorder(firstChild[node])
        print(alpha[node],end="")
        inorder(secondChild[node])

import sys
sys.stdin = open('중위_input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    firstChild = [0] * (N + 1)
    secondChild = [0] * (N + 1)
    alpha = [0] * (N + 1)
    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        ch = temp[1]
        alpha[addr] = ch
        if addr * 2 <= N:
            firstChild[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                secondChild[addr] = int(temp[3])

    print("#{}".format(tc), end=" ")
    inorder(1)
    print()