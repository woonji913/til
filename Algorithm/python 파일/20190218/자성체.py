import sys
sys.stdin = open("자성체_input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(N)
    # print(arr)

    cnt = 0
    for i in range(N):
        charge = 0
        for j in range(N):
            if arr[j][i] == 1:
                charge = 1
            elif arr[j][i] == 2:
                if charge == 1:
                    cnt += 1
                    charge = 0


    print(f"#{tc} {cnt}")
