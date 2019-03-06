N = int(input())
number = [input().split() for _ in range(N)]
score = [[0 for _ in range(3)] for _ in range(N)]
print(score)

game1 = []
game2 = []
game3 = []
for i in range(N):
    # 1게임
    game1.append(number[i][0])
    # 2게임
    game2.append(number[i][1])
    # 3게임
    game3.append(number[i][2])

print(game1)
print(game2)
print(game3)

for i in range(N):
    for x in game1:
        if game1.count(x) < 2:
            score[i][0] = int(x)
        else:
            score[i][0] = 0


for i in range(N):
    for x in game2:
        if game2.count(x) < 2:
            score[i][1] = int(x)
        else:
            score[i][1] = 0

for i in range(N):
    for x in game3:
        if game3.count(x) < 2:
            score[i][2] = int(x)
        else:
            score[i][2] = 0

print(score)


