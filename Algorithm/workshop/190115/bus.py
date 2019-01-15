import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    idx = 0 #시작점
    count = 0 #충전소 만난 횟수
    while idx+K < N: #현재위치 + 한번 이동거리가 종점되면 종료!
        for i in range(idx+K, idx, -1): #이동거리내에서 가장 먼 충전소부터찾기
            if i in charge:
                idx = i #충전소 만나면 현재위치를 만난 충전소위치로 변경
                count += 1  #충전소만난횟수+1
                break
        else:
            print(f"#{test_case} 0")    #for문 빠져나간다는말은 결국 충전소가 거리내에 없다는것
            break
    else:
        print(f"#{test_case} {count}") #while빠져나간다는말은 종점도착할 수 있다는말

