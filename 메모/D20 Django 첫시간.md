# D20 Django

### 0. 준비사항

1. pyenv/python/pyenv-virtualenv 설치 및 설정

   * python 3.6.7

   * git
2. 가상환경 생성
```bash
https://gist.github.com/edujunho/bee20c196ecacc3e8cdf068b4ec64d9f 참고
```

3. 프로젝트 폴더 생성 및 이동
4. local 가상환경 활성화
5. 장고 설치

### 1. Django Start

#### 1.1 장고 프로젝트

1. 프로젝트 생성

   > django, test, class, django-test는 프로젝트 이름으로 사용하면 안된다.

   ```bash
   django-admin startproject first_workshop .
   ```


2. 서버실행

   > ALLOWED HOSTS = ['*']
   >
   > ALLOWED HOSTS = ['example.username.c9users.io']

3. .gitignore 설정

4. TIMEZONE / LANGUAGE_CODE 설정

5. 로켓 페이지 한글화 확인

6.  프로젝트 구조

   `manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티.

   `프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import할 수 있습니다.

   `setting.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다.

   `__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일.

   `urls.py` : 현재 장고 프로젝트의 url 선언을 저장. 사이트의 url과 views의 연결을 지정.

   `wsgi.py` : 현재 프로젝트를 서비스하기 위한 wsgi 호환 웹 서버의 진입점.

-----------------

#### 1.2 장고 어플리케이션(app)

* 실제로 특정한 역할을 하는 친구가 바로  app
* 프로젝트는 이러한 어플리케이션의 집합
* 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
* 각각의 어플리케이션은 MTV 패턴으로 구성되어 있다.
1. 어플리케이션 만들기
2. 어플리케이션 구조
* `admon.py` : 관리자용 페이지 커스터마이징 장소
* `app.py` : 앱의 정보가 있는 곳. 우리는 수정할 일이 없습니다.
* `models.py` : 앱에서 사용하는 model을 정의하는 곳.
* `tests.py` : 테스트 코드를 작성하는 곳.
* `views.py` : 뷰들이 정의 되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳.

3. 어플리케이션 등록

> home>apps.py>class HomeConfig()
>
> > `home.apps.HomeConfig` 등록
> >
> > 혹은 그냥 `home`이라고 작성 가능. 다만 추후에 자세한 설정을 할 수 없다.

---------------------------------------

### 2. MTV 패턴



-------------------------------------

### 3. view - urls

우리는 앞으로

1. views
2. urls
3. template 순 으로 코드를 작성할 겁니다.

* HttpResponse로 첫 리턴 값 출력해보기
* path(route, views, name) 2개의 필수인수와 1개의 선택인수
* 저녁 메뉴 리턴 실습

--------------------------------

### 4. templates

- 장고에서 사용되는 템플릿은 DTL(Django Template Language)이다.
- jinja2와 문법이 유사하지만 다르다.

#### 4.1 Template Variable

* render()
  * rendert(**request**, **template_name**, **context=None**, content_type=None, status=None, using=None)

#### 4.2 Variable Routing

```python
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
```

------------------------------------

### 5. Form data (get/post)

```python
request.GET.get('data')

request.POST.get('data')

{% csrf_token %}을 form 안에서 같이 보내줘야 합니다.
```

> csrf 공격과 같은 보안과 관련된 사항은 settings에 MIDDLEWARE에 되어 있다.
>
> 실제로 요청은 미들웨어 설정 사항들을 순차적으로 거친다. 응답은 아래에서 위로 거쳐서 응답이 리턴된다.

----------------------

### 6. Template Inheritance

home/templates/base.html 생성

```html
{% extends "base.html" %}
{% block title %}STUDENT{% endblock %}
{% block body %}
    <h1>내용</h1>
{% endblock %}
```

