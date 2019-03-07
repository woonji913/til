N = int(input())
Field = [list(map(int, input())) for _ in range(N)]

# print(Field)
ans = 0
def apple(x, y):
    sum_list = []

    cnt = 0
    for i in range(x+1):
        for j in range(y+1):
            if Field[i][j] == 1:
                cnt += 1
    sum_list.append(cnt)

    cnt = 0
    for i in range(x+1):
        for j in range(y+1, N):
            if Field[i][j] == 1:
                cnt += 1
    sum_list.append(cnt)

    cnt = 0
    for i in range(x+1, N):
        for j in range(y+1):
            if Field[i][j] == 1:
                cnt += 1
    sum_list.append(cnt)

    cnt = 0
    for i in range(x+1, N):
        for j in range(y+1, N):
            if Field[i][j] == 1:
                cnt += 1
    sum_list.append(cnt)

    for i in range(len(sum_list)):
        if sum_list[i] != sum_list[0]:
            return 0
    return 1

for i in range(N):
    for j in range(N):
        ans += apple(i, j)

if ans == 0:
    print(-1)
else:
    print(ans)
