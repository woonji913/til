import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = list(range(1, 13))
    n = len(arr)

    cnt = 0

    for i in range(1 << n):
        a = 0
        arr_p = []
        for j in range(n):
            if i & (1 << j):
                a += arr[j]
                arr_p.append(arr[j])
        # print(arr_p)

        if len(arr_p) == N:
            if a == K:
                cnt += 1
                # print(arr_p)
    print(f'#{tc} {cnt}')