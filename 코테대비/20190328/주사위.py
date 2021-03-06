def dfs(n):
    if n > N:
        if sum(rec) == M:
            print(*rec[1:N+1])
        return
    for i in range(1, 7): # 눈
        rec[n] = i
        dfs(n + 1)

N, M = map(int, input().split())
rec = [0]*8
dfs(1)


# # 주사위 강사님코드
#
# # 눈의 중복을 허용한 중복순열
# def dfs(no):
#     if no>N:
#         for i in range(1, N+1):
#             print(rec[i], end=" ")
#         print()
#         return
#     for i in range(1, 7):
#         rec[no] = i
#         dfs(no+1)
#
# # 눈의 중복을 배제한 순열
# def dfs2(no):
#     if no>N:
#         for i in range(1, N+1):
#             print(rec[i], end=" ")
#         print()
#         return
#     for i in range(1, 7):   # 눈
#         if chk[i]:
#             continue
#         chk[i] = 1  # 눈사용 체크
#         rec[no] = i
#         dfs2(no+1)
#         chk[i] = 0  # 눈 사용체크 해제
#
# # 눈의 합이 M인 경우만 인쇄
# def dfs3(no, nsum):
#     if no>N:
#         if nsum==M:
#             for i in range(1, N+1):
#                 print(rec[i], end=" ")
#             print()
#         return
#     for i in range(1, 7):
#         rec[no] = i
#         dfs3(no+1, nsum+i)
#
# # main ----------------------------
# N, M = map(int, input().split())
# rec = [0]*8 # 주사위별 눈 기록배열
# chk = [0]*7 # 눈 사용여부 체크배열
# # dfs(1)    # 1번 주사위부터 시작
# # dfs2(1)
# dfs(1, 0)   # 1번주사위부터 시작, 합계는 0
