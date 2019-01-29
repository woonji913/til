import sys
sys.stdin = open("회문_input.txt", "r")

def H_str(str_data, n, m):
    for i in range(n):
        for j in range(n-m+1):
            if str_data[i][j:j+m] == str_data[i][j:j+m][::-1]:
                return str_data[i][j:j+m]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # print(N, M)
    data = [input() for i in range(N)]
    data2 = [''.join([data[y][x] for y in range(N)]) for x in range(N)]

    # print(data)
    print(data2)


    a = H_str(data, N, M)
    b = H_str(data2, N, M)

    # print(a)
    # print(b)

    if a:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} {b}')


























    # for x in range(len(data)):
    #     for i in range(N // 2):
    #         if data[x][i] == data[x][-1-i]:
    #             print(data[x])
    #         if data[x][i] == data[-1-x][i]:
    #             print(data[x][i])


