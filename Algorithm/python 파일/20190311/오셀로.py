for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list([0] * N for n in range(N))
    S = N // 2
    arr[S][S] = 2
    arr[S - 1][S] = 1
    arr[S][S - 1] = 1
    arr[S - 1][S - 1] = 2
    

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    for m in range(M):
        i, j, s = map(int, input().split())
        i -= 1
        j -= 1
        arr[i][j] = s
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            stack = []
            while 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] != s:
                    stack.append(ni)
                    stack.append(nj)
                elif arr[ni][nj] == s:
                    while stack:
                        rj = stack.pop()
                        ri = stack.pop()
                        arr[ri][rj] = s
                    break
                ni += di[k]
                nj += dj[k]

    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B += 1
            elif arr[i][j] == 2:
                W += 1
    print('#{} {} {}'.format(tc, B, W))