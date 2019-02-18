import sys
sys.stdin = open("자성체_input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        charge = 0
        for j in range(N-1, -1, -1):
            if arr[j][i] == 2:
                charge = 2
            elif arr[j][i] == 1:
                if charge == 2:
                    cnt += 1
                    charge = 0

    print(f'#{tc} {cnt}')