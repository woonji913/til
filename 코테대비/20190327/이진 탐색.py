def binarySearch(data, number):
    start = 0
    end = len(data)-1
    while start <= end:
        middle = (start+end)//2
        if number == data[middle]:
            return middle + 1
        elif number < data[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
data = list(map(int, input().split()))
T = int(input())
num = list(map(int, input().split()))

for i in num:
    print(binarySearch(data, i))