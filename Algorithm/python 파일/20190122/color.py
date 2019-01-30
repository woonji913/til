import sys
sys.stdin = open("color_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N= int(input())
    # print(N)
    square = [[0 for x in range(10)] for x in range(10)]
    cnt = 0

    for n in range(N):
        x1, y1, x2, y2, color = list(map(int, input().split()))

        if color == 1:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    square[i][j] += 1
                    if square[i][j] == 3:
                        cnt += 1
        if color == 2:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    square[i][j] += 2
                    if square[i][j] == 3:
                        cnt += 1

    print(f'#{tc} {cnt}')





