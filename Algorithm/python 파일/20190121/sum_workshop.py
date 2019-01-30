import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1):
    N = list(map(int, input().split()))
    arr = [[0 for i in range(100)] for i in range(100)]
    sum_array = []

    for i in range(100):
        arr[i] = list(map(int, input().split()))


# 행의 합
        sum_line = 0
        for j in arr:
            if sum_line < sum(j):
                sum_line = sum(j)

# 열의 합
        sum_row = 0
        for k in range(len(arr[0])):





