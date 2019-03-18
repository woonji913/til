import sys
sys.stdin = open("행렬input.txt", "r")

T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    hang = 0
    sumlist = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            hang += arr[i][j]
        sumlist.append(hang)
        hang = 0

    yeol = 0
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            yeol += arr[i][j]
        sumlist.append(yeol)
        yeol = 0

    daegak1 = 0
    for i in range(len(arr)):
        daegak1 += arr[i][i]
    sumlist.append(daegak1)
    daegak1 = 0

    daegak2 = 0
    for i in range(len(arr)):
        daegak2 += arr[-i][i]
    sumlist.append(daegak2)
    daegak2 = 0

    print("#{} {}".format(tc, max(sumlist)))


