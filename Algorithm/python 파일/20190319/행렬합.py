import sys
sys.stdin = open("행렬input.txt", "r")
#
# T = 10
# for tc in range(1, T+1):
#     t = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     # print(arr)
#
#     hang = 0
#     sumlist = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             hang += arr[i][j]
#         sumlist.append(hang)
#         hang = 0
#
#     yeol = 0
#     for j in range(len(arr[0])):
#         for i in range(len(arr)):
#             yeol += arr[i][j]
#         sumlist.append(yeol)
#         yeol = 0
#
#     daegak1 = 0
#     for i in range(len(arr)):
#         daegak1 += arr[i][i]
#     sumlist.append(daegak1)
#     daegak1 = 0
#
#     daegak2 = 0
#     for i in range(len(arr)):
#         daegak2 += arr[-i][i]
#     sumlist.append(daegak2)
#     daegak2 = 0
#
#     # print(sumlist)
#     print("#{} {}".format(tc, min(sumlist)))

# 아래는 홍용이꺼
for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    
    sum = []
    line_m, line_n, line_mn, line_nm = 0, 0, 0, 0
    for x in range(len(data)):
        line_mn += data[x][x]
        line_nm += data[x][99 - x]
    sum.append(line_mn)
    sum.append(line_nm)

    for x in range(len(data)):
        line_m, line_n, line_mn, line_nm = 0, 0, 0, 0
        for y in range(len(data[0])):
            line_m += data[x][y]
            line_n += data[y][x]
        sum.append(line_n)
        sum.append(line_m)

    print("#{} {}".format(test_case + 1, min(sum)))