N = int(input())
maeul = [list(map(int, input())) for _ in range(N)]

print(maeul)

vils = []
for i in range(N):
    for j in range(N):
        if maeul[i][j] == 2:
            x, y = i, j
        elif maeul[i][j] == 1:
            vils.append([i, j])

maxd = 0
for vil in vils:
    [i, j] = vil
    d = ((i-x)**2 + (j-y)**2)**0.5

    if maxd < d:
        maxd = d

# print(int(maxd) + (maxd%int(maxd) > 0))

if max > int(max):
    print(int(max)+1)
else:
    print(int(max))