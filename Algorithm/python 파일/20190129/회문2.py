import sys
sys.stdin = open("회문2_input.txt", "r")

def H_str(str_data, n, m):
    for i in range(n):
        for j in range(n-m+1):
            if str_data[i][j:j+m] == str_data[i][j:j+m][::-1]:
                return str_data[i][j:j+m]

T = 10
for tc in range(1, T + 1):
    N = input()
    data = [input() for i in range(100)]
    # print(data)
    data2 = [''.join([data[y][x] for y in range(100)]) for x in range(100)]
    # print(data2)

    ans = []
    for m in range(100):
        a = H_str(data, 100, m)
        b = H_str(data2, 100, m)
        ans.append(a)
        ans.append(b)
        data3 = list(set(ans))
    data3.remove(None)

    len_num = []
    for i in data3:
        len_num.append(len(i))

    print(f'#{tc} {max(len_num)}')


