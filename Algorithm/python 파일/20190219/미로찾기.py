import sys
sys.stdin = open("미로_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    # print(data)

