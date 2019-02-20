# import 순서
# 1. 파이썬 표준 라이브러리 ex) os, random....
# 2. core django : 장고 프레임워크에 내장되어 있는 것
# 3. 3rd party library : pip로 설치한 것들.(외적 설치) ex) django-extention...
# 4. 장고 프로젝트 app

from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-id') # 받아올 때부터 정렬 바꿔서 보내줌
    # boards = Board.objects.all()[::-1] # 원래 결과를 파이썬이 변경
    return render(request, 'boards/index.html', {'boards': boards})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    # Board.objects.create(title=title, content=content)
    # 위에 두 줄 한줄로 만들기
    
    # return render(request, 'boards/index.html')
    # 처음에 글이 보이지 않았던 이유는 보여지는 페이지 자체를 index이지만 index의 url로는 돌아가지 못했기 때문이다.
    # 즉, 단순히 html문서만 보여준 것이다. create는 model에 record를 생성하라는 요청이기 때문에, 단순히 페이지를 달라고 하는
    # GET방식 보다는 POST가 의미상 더 적절하다.
    # (그리고 모델과 관련된 데이터이기 떄문에 url에 직접 보여지는 것은 좋지 않다.)
    
    return redirect('/boards/')
    # return redirect(index)