import sys
sys.stdin = open("screw_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    data = [[0 for _in range(2)] for _ in range(N)]
    ans = [0] * 2 * N
    pos = 0
    for i in range(N):
        for j in range(2):
            data[i][j] = temp[pos]
            pos += 1

    #시작찾기
    spos = 0
    while (spos < N):
        j = 0
        while(j < N):
            if data[spos][0] == data[j][i]:
                break
            j += 1
        if j == N : break
        spos += 1

    #ans list에 저장하기
    pos = 0
    ans[pos] = data[spos][0]
    pos += 1
    ans[pos] = data[spos][1]
    while (1):
        for i in range(N):
            if ans[pos] == data[i][0]:
                pos += 1
                ans[pos] = data[i][0]
                pos += 1
                ans[pos] = data[i][1]
        if pos == 2 + N - 1:
            break

    print("#{}".format(tc), end=" ")