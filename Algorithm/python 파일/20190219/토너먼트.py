import sys
sys.stdin = open("토너_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = input().split()
    print(data)

    vic_cycle = {'1': '2', '2': '3', '3': '1'}
    for i in range(N-1):
        if i < N//2:
            if vic_cycle[data[i]] == data[i + 1]:
                print(data[i+1])
            else:
                print(data[i])

        else:
            if vic_cycle[data[i]] == data[i + 1]:
                print(data[i + 1])
            else:
                print(data[i])