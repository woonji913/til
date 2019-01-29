import sys
sys.stdin = open("회문_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(N, M)
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(input())
