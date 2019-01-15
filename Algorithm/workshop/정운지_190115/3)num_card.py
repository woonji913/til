import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, list(input())))
    # print(data)
    count_list = [0] * 10
    for i in range(len(data)):
        count_list[data[i]] += 1
    
    max_index = 0 # index
    max_value = 0 # 값

    for i in range(len(count_list)):
       if count_list[i] >= max_value: 
           max_value = count_list[i]
           max_index = i
      
    print(f"#{test_case} {max_index} {max_value}")