def check(m):
    # 상한액으로 지방에서 요청액을 배정가능하면 배정하고 아니면 상한액으로 합계계산
    # 합계가 총액 이하이면 성공 아니면 실패 리턴
    total = 0
    for i in range(N):
        if data[i] <= m:
            total += data[i]
        else:
            total += m
    if total <= M:
        return 1
    else:
        return 0

N = int(input())
data = list(map(int, input().split()))
M = int(input())

e = max(data)
s = 1
sol = 0
while s <= e:
    # 1원에서 max원까지 상한가를 mid로 결정하여 총액이하이면 상한액을 늘리고 아니면 줄임
    m = (s+e)//2
    if check(m):
        # 성공하면 상한액을 늘림
        sol = m
        s = m+1
    else:
        # 초과하면 상학액을 줄임
        e = m-1
print(sol)