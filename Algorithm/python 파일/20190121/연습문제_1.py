# 25개의 숫자 5x5 2차 배열
def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calAbs(y, x):
    if y -x > 0:
        return y - x
    else:
        return x - y

# arr = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
arr = [[0 for k in range(5)] for k in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
# print(arr)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])
print("sum = {}".format(sum))