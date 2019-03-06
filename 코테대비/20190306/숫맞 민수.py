# 2차원 행렬 만들기
X = int(input())
data = [[0 for x in range(3)] for x in range(X)]
for i in range(X):
    data[i] = list(map(int, input().split()))

# 열 순회
# 한열 돌때마다 리스트 만들고 팝으로 뽑은 숫자가 리스트 안에 없으면 결과값에 더한다
# 열 순회 끝나면 result로 한 사람 결과값 출력
# 열마다 리스트 만들어야 하니 3*사람수만큼 리스트 만들어야함ㅋㅋㅋㅋ 비효율 쩜
for people in range(X):
    result = 0
    for j in range(len(data[0])):
        check = []
        for i in range(len(data)):
            check.append(data[i][j])
        num = check.pop(people)
        if num not in check:
            result += num
    print(result)