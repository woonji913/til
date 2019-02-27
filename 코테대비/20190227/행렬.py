x, y= map(int, input().split())
data = [list(map(int, input().split())) for _ in range(x)]
# print(data)
for i in range(len(data)):
    cnt = 1
    for j in range(len(data[i])-1):
        if data[i][j] != 0 and data[i][j+1] == 1:
            cnt += 1
            data[i][j+1] = cnt

        elif data[i][j] != 0 and data[i][j+1] == 0:
            cnt = 1

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()


