# (django) 테스트

190418

### * 중요사항

* 문제의 버그를 얼마나 빠르고 **정확**하게 하는지 제출속도를 채점요소 포함

* 웹 서칭, 공유 금지

* 재시험 있음

* 시험시간 2시간 (강사님들 15~25분 걸리심 / 보통 1시간반)

* 시험범위 : 게시글 - 댓글, 로그인 - 로그아웃

  * 가장 기본부터 1 : N까지 발생하는 오류들

  * 단, 로그인, 로그아웃은 직접 바닥부터 짤 필요 없다.
  * ===디버깅 퀘스트 범위 안내===
    Django에서 가장 기본인 1:N 까지 범위에서 발생하는 오류들
    1. Django 기본 설정(settings.py) - Internationalization / static files / templates 등
    2. 템플릿 활용
    3. 게시글-댓글 관계(CRUD) 과정에서 사용된 내용(모델/모델폼 등)
    4. 로그인, 로그아웃
      단, 모든 코드는 직접 바닥 부터 짤 필요는 없다. (edited) 

##### 예시

1. 오류 메세지가 없는 경우 (아무것도 안뜰 때. - 템플릿 문제)

   인덱스 페이지가 안떳을때(로그인, 회원가입 부분은 남아있음) - **db문제가 아님**, 템플릿 문제

   1) base.html 부터 확인

   2) index.html 확인 ({% block body %}와 {% block content %}이런것도 꼼꼼하게 보기.)

2. NoReverseMatch

   1) 오류 메세지 보기.

   2) url 확인하고 경로 찾기.

   3) 에러 역추적하기

3. django 에러가 불친절 할 경우 터미널 에러도 확인하기.

________________________

### * 월요일 - DB 시험 (SQL + ORM)

* 객관식 / 단답형

* 공부 마크다운

<https://github.com/djpy2/TIL/tree/master/SQL>

<https://github.com/djpy2/TIL/tree/master/ORM>

https://github.com/djpy2/Django/blob/master/documents/Django_M_N_Relationship.md

* 예시문제를 보고싶다면 아래

<https://github.com/djpy2/Django/blob/master/documents/Django_Model_Relationship_Review.md>



________________________

### * 금요일 - django 월말평가

* 객관식 / 단답형
* django 전체범위