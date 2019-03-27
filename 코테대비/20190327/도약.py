def bns_up(s, e, d):
    sol = -1

    while s <= e:
        m = (s + e) // 2
        if point[m] < d:
            s = m + 1
            sol = m + 1
        else:
            e = m - 1
    return sol

N = int(input())
point = sorted([int(input()) for _ in range(N)])

ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        jump = point[j] - point[i]
        ans += bns_up(1, N-1, point[j]+ (2 * jump) + 1) - bns_up(1, N-1, point[j] + jump)

print(ans)