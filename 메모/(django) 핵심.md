```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # signup을 하면 자동로그인이 되도록
            auth_login(request, user)
            return redirect('posts:list')
            
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)

    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    context = {'form' : form,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
```





```python
# posts/views.py
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import PostForm
from .models import Post

def list(request):
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    context = {'post_form': post_form,}
    return render(request, 'posts/form.html', context)
    
@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form,}
    return render(request, 'posts/form.html', context)
    
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')

# 1
@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')

# 2
@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
		user = request.user
    # 이미 해당 유저가 like 를 누른 상태면 좋아요 취소(해당 유저가 like_users 컬럼에 존재하면 해당 유저를 지움)
    if post.like_users.filter(pk=user.pk).exists():
        post.like_users.remove(user)
    # 안 눌렀다면 좋아요
    else:
        post.like_users.add(user)
    return redirect('posts:list')
```





```python
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
{% if request.resolver_match.url_name == 'create' %}
    <h1>NEW</h1>
{% else %}
    <h1>EDIT</h1>
{% endif %}

<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ post_form }}
    <input type='submit' value='submit'/>
</form>

<a href="{% url 'posts:list' %}" class="btn btn-info">Back</a>
{% endblock %}
```

