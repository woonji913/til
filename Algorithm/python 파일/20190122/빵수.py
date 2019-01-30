import sys
sys.stdin = open("color_input.txt", "r")

T = int(input())
for case in range(T):
    N = int(input())
    count = 0
    template = [[0 for i in range(10)] for i in range(10)]
    for color_case in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for rcolor in range(r1,r2+1):
                for ccolor in range(c1,c2+1):
                    template[rcolor][ccolor] += 1

                    if template[rcolor][ccolor] == 3:
                        count += 1


        if color == 2:
            for rcolor in range(r1,r2+1):
                for ccolor in range(c1,c2+1):
                    template[rcolor][ccolor] += 2
                    if template[rcolor][ccolor] == 3:
                        count += 1
    print(f'#{case+1} {count}')