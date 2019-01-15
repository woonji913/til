import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    
    a, b = max(boxes), min(boxes)
    
    i = 0
    while i < N:
        if a - b <= 1:
            print(f"#{tc} {a - b}")
            break
        boxes[boxes.index(a)] -= 1
        boxes[boxes.index(b)] += 1
        a, b = max(boxes), min(boxes)
        i += 1

    else:
        print(f"#{tc} {a - b}")

        


