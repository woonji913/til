import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N):

        if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
            ans += data[i] - sorted(data[i-2])







print(f"#{tc+1} {ans}")