import sys
sys.stdin = open("binary_input.txt", "r")

def binarySearch(a, key):
    start = 0
    cnt = 0
    b = list(range(1, a+1))
    end = len(b) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == b[middle]: # 검색성공
            cnt += 1
            return cnt
        elif key < b[middle]:
            end = middle - 1
            cnt += 1
        else:
            start = middle + 1
            cnt += 1

    return -1 # 검색실패

T = int(input())
for tc in range(1, T + 1):
    To, A, B = map(int, input().split())
    if binarySearch(To, A) > binarySearch(To, B):
        winner = 'B'
    elif binarySearch(To, A) < binarySearch(To, B):
        winner = 'A'
    else:
        winner = '0'

    print(binarySearch(To, A))
    print(binarySearch(To, B))

    print(f'#{tc} {winner}')

