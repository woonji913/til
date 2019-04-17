# (django) 보충

190416 화요일

### * 학습목표

* (16일 수업) M : N 의 이해

* signup, login, create 코드의 흐름은 다 똑같다.



### 1. 오늘 수업 복습


* 코드 쿼리셋(Queryset) 쪼개보기

```python
post.image_set.first.file.url
# 만약 이미지가 없어서 오류가 난다면 .file~에서 난다.
# post.image_set.first 는 하나의 쿼리셋으로 보내지기 때문
# 이 때 오류는 None오류가 난다.
```

```python
# 1번 글의 두번째 댓글을 쓴 사람의 첫번째 게시물의 작성자의 이름
user_id = post.comment_set.all()[1].user.post_set.first.user.name
# LIMIT 1 OFFSET 1

# django에서 쿼리문을 날리는 시점(호출되는 시점) >> [1]을 만났을때.
```

* M 대 N

  중개모델 (Intermediary Model) : 두개의 table을 이어주는 역할.

  * 역참조 사용으로 중개모델을 따로 만들 필요 없어짐.
  * ![중개모델](C:\Users\student\Desktop\woonji\til\메모\중개모델.png)

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.TextField()
    # doctors = models.ManyToManyField(Doctor, related_name='patients') # 얘가 역참조
    
    def __str__(self):
        return self.name

# 얘가 중개모델 / 역참조를 사용한다면 굳이 필요없다.
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

* template tag (gravatar 할때 했음. project04 - accounts - templatetags에 있음.)

```python
import hashlib # django의 템플릿 내놔!
from django import template
# from django.template.defaultfilters import stringfilter

# 템플릿 라이브러리 가져와
register = template.Library()

# 필터로 makehash 함수를 추가해
@register.filter
# @stringfilter
def makemd5(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
```



### 2. crud 짜기 (흐름이 중요)

```python
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from .models import Post
```

* import는 코드를 짜면서 차차 추가하기



* list 만들기 : `def list(request):` 쓰고 바로 경로 만들어주기(`urls.py`)

```python
def list(request):
    posts = Post.objects.all()
    context = {'posts':posts,}
    return render(request, 'posts/list.html', context)
```

```html
{% extends 'base.html' %}
{% block content %}
<a href="{% url 'posts:new' %}">새글쓰기</a>
{% endcontent %}
```

* create 만들기 : `list.htm`l에 a링크로 새글쓰기 링크 만들어주기

```python
urls.py

path()
```

* views.detail

```python
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)
```

* detail.html

```html
{% extends 'base.html' %}
{% block content %}
	{{ post.pk }}
{% endcontent %}
```

* views.delete

```python
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:list')
```

>  이 순서에서 `redirect` import해주기

#### * update (흐름을 보기)

1. views.update

```python
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    # 수정요청이라는 것은 form을 던져줬을때 거기에서 수정을 하고 다시 던져주면 저장하는 것.
    context = {'post':post}
    return render(request, 'posts/edit.html', context)
```

* forms.py

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
```

>  modelform을 만드는 이유 : field를 새로 작성할 필요 없이 모델에서 그대로 가져올 수 있어서.

* views.update

```python
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    # 수정요청이라는 것은 form을 던져줬을때 거기에서 수정을 하고 다시 던져주면 저장하는 것.
    post_form = PostForm(instance=post) 
    context = {'post':post, 'post_form':post_form}
    return render(request, 'posts/edit.html', context)
```

* edit.html

```html
<form method="POST">
    {% csrf_token %}
    {{ post_form }}
    <input type="submit" value="submit"/>
</form>
```

2. 사용자가 보내준 값을 받기 (if문 넣기)

```python
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        # 수정요청이라는 것은 form을 던져줬을때 거기에서 수정을 하고 다시 던져주면 저장하는 것.
        post_form = PostForm(instance=post) 
        # 검증
        if post_form.is_valid():
            post = post_form.save()
            return redirect('posts:detail', post_pk)
    post_form = PostForm(instance=post)
    context = {'post':post, 'post_form':post_form}
    return render(request, 'posts/edit.html', context)
```

3. commit=False의 시점은 언제인가?

```python
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        # 수정요청이라는 것은 form을 던져줬을때 거기에서 수정을 하고 다시 던져주면 저장하는 것.
        post_form = PostForm(instance=post) 
        # 검증
        if post_form.is_valid():
            # post = Post()
            # post.title = request.POST.get('title')
            # post.content = request.POST.get('content')
            # ================ (시점) commit=False ==================
            # post.user = request.user
            # post.save()
            post = post_form.save(commit=False) 
            # 혹시 모르겠는 경우 : 검색어 modelform notsave 이런식으로 해야됨
            post.user = request.user
            post.save()
            return redirect('posts:detail', post_pk)
    post_form = PostForm(instance=post)
    context = {'post':post, 'post_form':post_form}
    return render(request, 'posts/edit.html', context)
```



### 3. 코드의 흐름

* create, update, signup, login의 코드의 흐름은 똑같다!

  1) if method가 `post 방식`인지 확인하고 → `form` 던져주고 → 유효성(`is_valid()`) 검증하고 → 리턴 리다이렉트


​       2) else method 가 `get방식`일 경우 →  그냥 `form`만 던져주기 → 리턴 렌더



### 4. 쿠키와 session

HTTP의 특성

* connectless  : 계속 연결되어 있지 않다.

* stateless : 얘의 상태를 알 수 없다.

요청하기 전까지는 응답할 수 없다.

> 그래서 나온 것이 `Cookie`

어떠한 정보를 사용자가 주면 우리에게 쿠키를 준다. 

(쇼핑몰의 장바구니도 쿠키임 → 쿠키삭제하면 장바구니 비워짐)

> 보완이 취약한 특성이 있다. 그래서 나온 것이 `Cookie` →`Session` 



session은 내 정보를 서버에 저장해서(보안된 정보) 쿠키와 정보가 같은지 확인하는 것.

> 서버에 저장하는 것이기 때문에 굳이 장바구니 같은 것은 session에 저장하지 않는다.

> 비행기표를 볼때 시크릿 모드로 봐라 (시크릿모드는 쿠키를 저장해두지 않음)