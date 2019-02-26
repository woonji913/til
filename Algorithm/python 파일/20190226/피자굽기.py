# import sys
# sys.stdin = open("피자_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     pizza = list(map(int, input().split()))
#
#     print(N, M)
#     print(pizza)
#
#


def oven(pizza):
    global N

    # Q에 피자추가
    Q = []
    for i in range(N):
        # 좌표, 치즈
        Q.append([i, pizza.pop(0)])
        visited[i] = 1

    # 좌표 가중치 설정
    ci = 0

    # oven 안에 pizza가 있는 동안 loop
    while 1 in visited:
        for i in range(N):
            # 치즈 사망
            Q[i][1] = Q[i][1] // 2
            # 치즈가 0일때
            if Q[i][1] == 0:
                if pizza:
                    # 피자빼기
                    visited[Q[i][0]] = 0
                    Q[i] = [0,0]
                    # 피자넣기
                    visited[N+ci] = 1
                    Q[i] = [N+ci, pizza.pop(0)]
                    ci += 1
                else:
                    visited[Q[i][0]] = 0
                    # 마지막에 나오는 pizza
                    if 1 not in visited:
                        return Q[i][0] + 1
                    # oven 비우기
                    Q[i] = [0,0]


import sys
sys.stdin = open('피자_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    visited = [0]*len(pizza)

    print(f'#{tc} {oven(pizza)}')