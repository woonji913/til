import sys
sys.stdin = open("최소신장트리.txt", "r")


def findset(x):
    if x == p[x]: return x
    else: return findset(p[x])

def mst():
    global V
    c = 0   # 간선개수
    s = 0   # 가중치의 합
    i = 0   # 제어변수

    while c < V:                    # MST 구성을 위해 V 개의 간선
        p1 = findset(data[i][0])    # 두 노드의 대표원소 알아내기
        p2 = findset(data[i][1])
        if p1 != p2:                # 사이클이 생성되지 않으면
            s += data[i][2]         # MST에 포함되므로 가중치 추가
            c += 1                  # 간선 개수 증가
            p[p2] = p1              # 대표 원소 관리
        i += 1                      # 저장된 다음 간선으로 이동
    return s                        # MST 완성 후 가중치 합 변환

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]

    # make set
    p = list(range(V + 1))

    # 가중치를 sort
    data.sort(key=lambda x: x[2])
    print('#{} {}'.format(tc + 1, mst()))