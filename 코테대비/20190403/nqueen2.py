# nQueen
# http://comganet.github.io/dfs/2016/06/03/dfs-1000

N = int(input())
sol = 0
chs = [[0]*N for _ in range(N)]

chk1 = [0] * (N + 1)
chk2 = [0] * (N*2 + 1)
chk3 = [0] * (N*2 + 1)

def dfs(n):
    global sol

    if n == N:
        sol += 1
        return
    for i in range(N):
        if chk1[i]: continue
        if chk2[n + i]: continue
        if chk3[N-1-(n-i)]: continue

        chk1[i] = 1
        chk2[n + i] = 1
        chk3[N - 1 - (n - i)] = 1

        dfs(n+1)

        chk1[i] = 0
        chk2[n + i] = 0
        chk3[N - 1 - (n - i)] = 0

dfs(0)

print(sol)