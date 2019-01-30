import sys
sys.stdin = open("special_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    n = len(data)

    for i in range(n):
        if i % 2 == 0:
            max = i
            for j in range(i+1, n):
                if data[max] < data[j]:
                    max = j
            data[i], data[max] = data[max], data[i]
        else:
            min = i
            for k in range(i+1, n):
                if data[min] > data[k]:
                    min = k
            data[i], data[min] = data[min], data[i]

    print(f'#{tc}',end=' ')
    for i in range(10):
        print(data[i], end=' ')
    print()
