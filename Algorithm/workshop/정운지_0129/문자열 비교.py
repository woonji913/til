import sys
sys.stdin = open("문자열 비교_input.txt", "r")

def BF(list1, list2):
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] != list2[j]:
            j = j - i
            i = -1
        j = j + 1
        i = i + 1
    if i == len(list1):
        return j - len(list1)  # 검색 성공
    else:
        return -1  # 검색 실패

T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    dum_list = list(input())
    # print(string)
    # print(dum_list)

    if BF(string, dum_list) == -1:
        ans = 0
    else:
        ans = 1


    print(f"#{tc} {ans}")