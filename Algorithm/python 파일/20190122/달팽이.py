import sys
sys.stdin = open("color_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for x in range(10)] for x in range(10)]
    for i in range(N):
        a1, b1, a2, b2, color = list(map(int, input().split()))

        print(a1, b1, a2, b2, color)