import sys
sys.stdin = open("GNS_input.txt", "r")

T = int(input())
for tc in range(T):
    temp = input()
    data = list(map(str, input().split()))
    n = len(data)
    # print(data)
    # print(len(data))
    dict_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3,
     "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    num_list = []
    for i in data:
        num_list.append(dict_num[i])

    a = sorted(num_list)

    dict_num_rev = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR",
                4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

    data_list = []
    for x in a:
        data_list.append(dict_num_rev[x])

    # print(data_list)
    # print(' '.join(data_list))

    print(f"#{tc+1}")
    print(' '.join(data_list))




