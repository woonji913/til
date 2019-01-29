import sys
sys.stdin = open("회문2_input.txt", "r")

T = 10
for tc in range(1, T+1):
   # 데이터 받기
    N = int(input())
    data = [[0 for x in range(N)] for x in range(N)]
    for i in range(N):
        data[i] = list(input())
   # print(N, M)
   # print(data)


   # 행 방향 탐색
    for x in range(len(data)):
        row = []
        for y in range(len(data[x])):
            row += data[x][y]
            count = 0
        for M in range(100):
            for idx in range(100-M+1):
            M_list = []
            if row[idx] == row[idx + M - 1]:
                M_list = row[idx:idx + M]
                result = row[idx:idx + M]
                for i in range(len(M_list)//2):
                    M_list[i], M_list[-1-i] = M_list[-1-i], M_list[i]
                if result == M_list:
                    result = ''.join(M_list)
                    print(f'#{tc+1} {result}')


   # 열 방향 탐색
    for y in range(len(data[0])):
        column = []
        for x in range(len(data)):
            column += data[x][y]
            count = 0
        for M in range(100):
            for idx in range(100-M+1):
                M_list = []
                if column[idx] == column[idx + M - 1]:
                    M_list = column[idx:idx + M]
                    result = column[idx:idx + M]
                    for i in range(len(M_list)//2):
                        M_list[i], M_list[-1-i] = M_list[-1-i], M_list[i]
                    if result == M_list:
                        result = ''.join(M_list)
                        print(f'#{tc+1} {result}')