20190108
# git 초기화
## 방법 1
폴더를 하나 만든다. -->ex)choi

cd desktop/choi로 이동한다.

github.com 들어가서 til의 클론을 복사한다.

git clone https://github.com/hongyong3/TIL.git을 한다.

cd desktop/choi/til로 들어가면 자동으로 git init 상태가 된다.

기존 사용자의 github정보를 지운다.

$ git credential reject        ------> 엔터
protocol=https                 ------> 엔터
host=github.com                ------> 엔터엔터엔터엔터
git push를 입력하면 로그인 창이 뜬다. --> 로그인하기

git config --global user.name 'hongyong3' --->commit 할때 본인 신분을 입력

git config --global user.email 'chy66822495@gmail.com'

git config --global --list ---> 본인이 입력한 것을 확인하기 위한 명령어

user.name=hongyong3 user.email=chy66822495@gmail.com -----> 다음과 같이 뜬다.

git config --global color.ui true -----> git 색칠해주는것.

다시 git config --global --list를 입력하여 확인.

user.name=hongyong3 user.email=chy66822495@gmail.com color.ui=true

git status를 입력하여

On branch master Your branch is up to date with 'origin/master'. nothing to commit, working tree clean

이 나와야 한다.

## 방법 2
이 명령어가 어려우면 제어판에 들어가서 범주를 큰아이콘
자격 증명 관리자에서 일반 자격 증명을 삭제한다.
#집에서 til이 git 되어 있을 경우
연수원 : TIL git push

집 : git pull 하고 나서 ---> add commit push를 해야한다.

다시 연수원에 오면

git pull / add commit push를 반복해야한다.

## git clone 서로 주고받기
git pull -> 수정하고 -> git add . -> git commit -m -> git push

서로 주고 받은 것 확인하려면 git log