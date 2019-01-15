#import sys
#sys.stdin = open("input.txt")

def findmaxmin(boxes):
    max_b = 0
    min_b = 0
    for i in range(len(boxes)):
        if boxes[max_b] < boxes[i]:
            max_b = i
        if boxes[min_b] > boxes[i]:
            min_b = i
    return [max_b, min_b]
for tc in range(1, 11):
    limit = int(input())-1
    boxes = list(map(int, input().split()))
    max_b = [0, boxes[0]]
    min_b = [0, max_b[1]]
    idx = findmaxmin(boxes)
    boxes[idx[0]] -= 1  # 최대값
    boxes[idx[1]] += 1  # 최소값
    while limit > 0:
        idx = findmaxmin(boxes)
        diff = boxes[idx[0]] - boxes[idx[1]]
        if diff <= 1:
            break
        else:
            idx = findmaxmin(boxes)
            boxes[idx[0]] -= 1  # 최대값
            boxes[idx[1]] += 1  # 최소값
        limit -= 1
    idx = findmaxmin(boxes)
    diff = boxes[idx[0]] - boxes[idx[1]]
 
    print(f"#{tc} {diff}")