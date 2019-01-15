for i in range(1, 11):
    howmany = int(input())
    boxes = list(map(int, input().split()))
    mickey, mini = max(boxes), min(boxes)
    n = 0
    while n < howmany:
        if mickey - mini <=1:
            print(f"#{i} {mickey- mini}")
            break
        boxes[boxes.index(mickey)] -= 1
        boxes[boxes.index(mini)] += 1
        mickey, mini = max(boxes), min(boxes)
        n += 1
    else:
        print(f"#{i} {mickey-mini}")