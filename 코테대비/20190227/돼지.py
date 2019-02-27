def pig(data):
    find = []
    for i in range(len(data)):
        if data[i][1] == 'Y':
            find.append(1)
        else:
            find.append(0)

    for k in range(len(find) - 1):
        if find.count(1) == 1:
            if find[-1] == 1:
                return data[-1][0]
            else:
                return 'F'
        elif find.count(1) == 0:
            return 'F'
        else:
            if find[k] == 1 and find[k + 1] == 0:
                return 'F'
            elif find[k] == 1 and find[k + 1] == 1:
                return data[k][0]

N = int(input())

data = [tuple(input().split()) for _ in range(N)]
data.sort()

if N == 0:
    print('F')
else:
    print(pig(data))