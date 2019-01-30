import sys
sys.stdin = open("screw_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    screw = list(map(int, input().split()))
    # print(screw)

    screw_box = []
    for i in range(len(screw)):
        if i % 2 == 0:
            screw_p = screw[i:i+2]
            screw_box.append(screw_p)
    print(screw_box)

    n = len(screw_box)
    # for j in range(n):
    #     for k in range(n):
    #         if j == k:
    #             continue











