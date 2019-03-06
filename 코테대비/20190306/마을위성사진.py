N = int(input())
maeul =[]
for i in range(N):
    maeul.append(list(map(int, input())))
print(maeul)

for h in range(N):#높이 0부터 시작
    flag=0
    for i in range(1,N-1):
        for j in range(1,N-1):
          if maeul[i][j]>h:#높이보다 크면
              flag = 1
              if maeul[i-1][j]>h and maeul[i+1][j]>h and maeul[i][j-1]>h and maeul[i][j+1]>h:
                  maeul[i][j]+=1

    if flag ==0: break
print(h)