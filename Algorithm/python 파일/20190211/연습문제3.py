T = 8
N = [[1, 2],[1, 3],[2, 4],[2, 5],[4, 6],[5, 6],[6, 7],[3, 7]]

L = [[0 for _ in range(8)] for _ in range(8)]
# visited = [0 for i in range(n)] # 방문처리
# print(L)

for i in N:
    L[i[0]][i[1]] = 1
    L[i[1]][i[0]] = 1

for j in range(8):
    print(j, L[j])

