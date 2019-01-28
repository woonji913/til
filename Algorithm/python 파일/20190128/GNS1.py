import sys
sys.stdin = open("GNS_input.txt", "r")

T = int(input())
for tc in range(T):
    temp = input() # 더미 데이터
    data = list(map(str, input().split()))
    n = len(data)

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    data_list = [0] * 10
    for i in range(n):
        if data[i] in num_list:
            data_list[num_list.index(data[i])] += 1

    print(f"#{tc+1}")
    for i in range(len(data_list)):
        print((num_list[i]+' ')*data_list[i])


