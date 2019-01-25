# 191218_W2C2_ pyformat /dropbox

```python
# python 과거 // 저 %s를 자주 바꾸어야할 때는 뒤의  one two만 바꾸면 됨
'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

#1 pyformat // . for 은 메소드임 (for (args))
#'{} {}'.format( 'one', 'two')
#처음에 오는 name 이 0번인데, 순서 바꾸고 싶으면 {}안에 숫자 넣기 {1}만 두개 쓰면 olivia 만 두번 나오겠지?

name = '빵수수'
e_name = 'Olivia'
print('안녕하세요. {1}입니다. My name is {0}'.format(name, e_name))

#2 f-string python 3.6
print(f'안녕하세요. {name}입니다. My name is {e_name}.')

#3 
name = '홍길이'
print("안녕하세요. " + name + "입니다.")
```



```python
# LOTTO # sort는 숫자를 순서대로 해주니까 필요하겠지? # random 함수를 불러와야지 얘가 알아듣겠지
import random
x = list(range(1,46))
lotto = random.sample(x,6)
lotto.sort()
print(f'오늘의 행운 번호는 {lotto}입니다.')

```



import os

1) os.chdir(r'폴더주소')

. 작업하고 있는 위치 변경

2) os.listdir('폴더주소')

. 지정된 디렉토리에서 





```python
# 1파일을 만들면서 열기 write // 글 쓰고 닫기
# open close 는 항상 나옴
f = open("new.txt<만들 파일 명>", "w")
f.write("Hello !!!")
f.close()

#2 with 는 if 랑 같은 거고, 끝나면 자동적으로 close 해줌
with open("new.txt", "w") as f:
    f.write("Ik ben moe!!!")



# 파일을 열고 내용을 가져오고 싶을 때
# f는 변수를 생성하는 것을 뜻함 // f가 아니어도 됨
# f {}은 {}안의 string을 계속 바꾸는 함수이니까
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()

with open("new.txt", "r") as f:
    data = f.read()
    print(data)
    
    
    
##4. 열어서 글을 여러줄 쓰게 한다음에 닫기
#다 쓴다음에 닫아주어야 함 
# for은 특정 구간 안에서 5번 돌아가라

f = open("new.txt", "w", encoding='utf-8')
for n in range(5):
    data = f"{n}번째 줄입니다.\n"
    f.write(data)
f.close()

#with로 했을 경우
with open("new.txt", "w", encoding='utf-8') as f:
    for i in range(5):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)
       
```

# writelines

```python
# menu = ["카레\n", "파스타\n", "탕수육\n"]
f = open("menu.txt","w", encoding='utf-8')
f.writelines(menu)
f.close()



with open("new.txt","w",encoding='utf-8') as f:
    menu = ["카레\n", "파스타\n", "탕수육\n"]
    f.writelines(menu)

```

range는 자리를 하나만 차지함// 하나의 메모리를 돌려가면서 사용함 list는 다 차지하고



#   GIT에 올리는 방법

* git status

* git add .

* git commit -m "hoy"  <-커밋 버전 만들기
* ls -al <- 모든 파일을 다 보여줌 
* 바탕화면에 되어있을 때 -> rm -rf  .git
* git log ------ 올리는 방법



write: 내용 작성, 덮어쓰기

writelines: 여러줄 작성

append : 내용 추가

### Readline

---

#READLINE(): 한 줄로 읽어서 리턴

#READLINES() : 파일 전체를 읽어서 list 형태로 리턴



python 들어가서 실행

대충 변수 하나 만들어서  ssafy = '      dgsga '

lstrip / rstrip 하고 마지막으로 .strip 하고 

exit



print - 그 안에 들어있는 것을 불러와서 출력해라이니까

```python
# readlines 파일 전체를 list 형태로 리턴???
with open("ssafy.txt", "r", encoding='utf-8') as f:	 
	lines = f.readlines()
	for i in lines:
		print(i.strip())
        
# 여기서 print ()괄호 안에 있는 것을 꺼내와서 출력해라인데 i 가 안들어가니까 lines 에 들어있는
전체를 불러오게된거임....
+ strip()을 안하면 엔터가 한줄씩 추가되서 나오게 됨



# ANSWER # 범위를 복수로 받고, 단수로 i를 받는 것 literal  객체를 라인즈에 넣어주고, 그걸 돌려서 하나씩 출력하기
with open("ssafy.txt", "r", encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		print(line.strip())
```

// 깨알 팁

ublock

momentum

wappalyzer - 사이트가 어떤 언어를 쓰는지 보여줌

octotree

turn off the lights

grammarly

youtube dark mode 

### requests

```python
없으면 pip
.text 하면 html이 줌

import requests

print(requests.get("https://www.naver.com").status_code)
# 저장한다 = 변수에 담아라 
# 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다
# import requests 하고서
# 정보를 출력하여 확인한다
# print(req)

beautifulsoup
import 
import from -- 임포트 싫으면 .을 쓰고 하면 됨  -> 코드 짧아짐 bs4를 불러왔읜까 bs4.을 안써도 됨
import requests as bus <-이름 바꿀 수 있음
from bs4 import BeautifulSoup
```

---

### select_one

하나만 찍어서 가지고 오기

### . select(selector)

리스트로 뽑아서  for  문 돌릴 때 사용 --- readlines 가 리스트 객체를 가지고 옴 // 마치  select가 가지고 오는거랑 똑같음 

객체 가져와서 - 포문 돌리고 - 00경로로 뽑을지  정해서 값을 출력하기

for 아래에서 뽑아오면 됨 

문서 안에 있는 특정 내용을 하나만 뽑아줘

예쁘게 꾸민게  soup임 //  id는 유일한 값이라 짧게 나옴



```python
import requests 
from bs4 import BeautifulSoup
#요청해서 변수에 담고 응답받고 #예쁘게 꾸며서 soup에 넣어줌 # 딱 하나만 찝어내서 불러오기
req = requests.get("http://www.wemakeprice.com/deal/adeal/4226254/100600/?source=mdeal&tab=&no=9").text
soup = BeautifulSoup(req, 'html.parser')
# copy selector로 하나 찝은 html 붙여넣기 하기
price = soup.select_one("#contents > div.content-main > div.deal_area > div > div.price_area.app.new > div.price_info.wprice > div.set_price_area > ul > li.sale > span.num")
# text만 불러와야하니까 넣는거 잊지 말기
print(price.text)


```

```python
#네이버 실시간 검색어 답안
import requests 
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'): 
    
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name} 입니다.')


```

"띄어쓰기" 하면 자식이 바로 아래 자식이 아니어도 상관없음

/>은 > 는 바로 하위 자식을 뜻함

띄어쓰기로 서로 다른 클래스를 구분



BeautifulSoup(끌어오는 대상 변수, 웹에서 쓰면 <속성>으로 가지고 와야 함)

// html값을 넣으라고, 뷰티플 속성이 저렇게 html 형태로 넣으라고 되어있음

띄어쓰기 



객체 oop 객체지향언어를 이해해야함 - 감만 있는 경우가 많고, 애매모호한 개념





 git init

 git commit

https://076923.github.io/posts/Python-25/



혀ㅑㅅ



git hub으로 이력서 하나 만들어서 올릴 수 있음