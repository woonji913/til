def magic(n):
    num = str(n)
    if len(num) < 2:
        return int(num)
    elif len(num) >= 2:
        start = int(num[0])
        for i in range(1, len(num)):
            start += int(num[i])

        if start < 10:
            return start
        else:
            return magic(str(start))

num_list = []
magic_list = []
N = int(input())
for i in range(N):
    n = int(input())
    num_list.append(n)
    magic_list.append(magic(n))

max = magic_list[0]
max_idx = 0
for i in range(1, len(magic_list)):
    if max < magic_list[i]:
        max = magic_list[i]
        max_idx = i
    elif max == magic_list[i]:
        if num_list[i] < num_list[max_idx]:
            max_idx = i

print(num_list[max_idx])
