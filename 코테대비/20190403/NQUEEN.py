# prec = [(행1, 0), (행2, 1) , ...   ] 퀸 위치 저장
# 순열로 행을 저장하니까 행, 열 중복 없음
def perm(no):
    global n, flag, cnt
    if no >= n:
        cnt += 1
        return
    for i in range(n):
        if a[i]: continue

        if no:
            flag = True
            # 대각선 체크
            # 지금까지 넣은 순열 / 앞으로 넣을 순열 (no, i) 차이 같으면 대각선
            for j in range(no):
                if abs(prec[j][0] - no) == abs(prec[j][1] - i):
                    flag = False

                # 대각선 아니면 순열 레코드에 저장
            if flag:
                prec[no] = (no, i)
                a[i] = 1
                perm(no + 1)
                a[i] = 0

            # 레코드 맨 처음값 저장
        else:
            prec[no] = (no, i)
            a[i] = 1
            perm(no + 1)
            a[i] = 0


# main-------------------------
n = int(input())
prec = [0] * n
cnt = 0
a = [0] * n
perm(0)
print(cnt)