# import sys
# sys.stdin = open("농작물input.txt")

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    # print(arr)
    a = N//2
    b = N//2
    result = 0
    for i in range(N):
        for j in range(a, b+1):
            result += arr[i][j]
            print(result)
        if i < N//2:
            a += -1
            b += 1
        else:
            a += 1
            b += -1

    print("#{0} {1}".format(n, result))