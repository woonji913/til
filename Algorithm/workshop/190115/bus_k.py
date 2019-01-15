K, N, M = map(int, input().split()) # K한번이동, 종점N, M충전기 갯수
C = list(map(int,input().split())) #충전소가 담긴리스트

   idx = 0 #시작점
   count = 0 #충전소 만난 횟수
   while idx+K < N: #현재위치 + 한번 이동거리가 종점되면 종료!
       for i in range(idx+K, idx, -1): #이동거리내에서 가장 먼 충전소부터찾기
           if i in C:
               idx = i #충전소 만나면 현재위치를 만난 충전소위치로 변경
               count += 1  #충전소만난횟수+1
               break
       else:
           print(f"#{test_case} 0")    #for문 빠져나간다는말은 결국 충전소가 거리내에 없다는것
           break
   else:
       print(f"#{test_case} {count}") #while빠져나간다는말은 종점도착할 수 있다는말
