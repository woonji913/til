# D27 Workshop

190409

* 아래의 회원가입 페이지는 django.contrib.auth.forms 안에 있는 UserCreationForm()
  을 활용한 것이다. 아래 페이지를 위한 view, url, template 을 작성하세요.

![1554791328345](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1554791328345.png)

1. view

```python
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()         #1
            auth_login(request, user)  #2
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)
```

2. url

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

3. template

```html
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}

<h1>회원가입</h1>

<form method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="submit"/>
</form>
{% endblock %}
```

