import sys
sys.stdin = open("글자수_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    ans = []
    for i in str1:
        ans.append(str2.count(i))

    print(f"#{tc} {max(ans)}")

