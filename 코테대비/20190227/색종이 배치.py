x1, y1, dx1, dy1 = map(int, input().split())
x2, y2, dx2, dy2 = map(int, input().split())

# if x1+dx1 == x2 and y1+dy1 == y2:
#     print('1')
# elif x1+dx1 > x2 or y1+dy1 > y2:
#     print('2')
# elif x1+dx1 > x2 and y1+dy1 > y2:
#     print('3')
# elif x1+dx1 < x2 and y1+dy1 < y2:
#     print('4')

x = set(range(x1, x1+dx1+1)) & set(range(x2, x2+dx2+1))
y = set(range(y1, y1+dy1+1)) & set(range(y2, y2+dy2+1))

if len(x) == 1 and len(y) == 1:
    print(1)
elif len(x) == 1 or len(y) == 1:
    print(2)
elif len(x) and len(y):
    print(3)
else:
    print(4)