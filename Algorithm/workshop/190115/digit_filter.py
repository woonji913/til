import sys
sys.stdin = open("input.txt", "r")

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    odd = list(map(int, input().split()))
    data = list(map(int, input().split()))
    N = odd[0]
    M = odd[1]
    
    sum_list = []
    for k in range(len(data)-M+1):
        sum_list.append(sum(data[k: k+M]))
        b = sum_list

    ans = BubbleSort(b)[-1]-BubbleSort(b)[0]
    print(f"#{test_case}  {ans}")