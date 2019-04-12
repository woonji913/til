# Create와 modelform

1. models.py

```python
from django.db import models

# Create your models here.
#MTV 패턴이라 가장 중요함
# DB 설계부터 하기 때문에 ERD를 그려서 
#게시글에 어떤 내용을 담을 수 있지? 어떤걸 쓸 수 있을까 -- 그래서 모델 작성 먼저가 중요한거임
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
```



2. views.py

```python
from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
# 원래 둘인데 결혼해서 한집에 살아서  헷갈리는거임
# 일단 사용자한테 정보를 받아야해 - 그럼 form을 던져줘야겠지?
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST) # 들어온 값을 통으로 넣기
        if form.is_valid(): # 검증하기 - 유효한 값이면 
            form.save() # 저장해야겠지?
            return redirect('posts/index') # 리턴의 위치 중요함  valid에 안걸리는 애가 튀어나오아ㅣㅆ으면 거기 들어가서 어딘가로 이동하게 됨
    else:
    # forms에서 만든거 불러오고
        form = PostForm()
    context = {'form': form}
    return render(request,'posts/create.html')
        # 근데 계속 form을 엄청 많이 만들어야하니까 귀찮음 내가 매번 다 치고 모델을 만들어야하니까
        # models 에 정의해놓은거 대로 알아서 만들어달라 - 일관성 유지 가능함, model form 내가 정의해놓은거 그대로 
        # forms.py 만 봐도 뭐를 만들었구나가 알 수 있음
```



3. forms.py

```python
from django import forms
from .models import Post
# 저 모델을 쓰려면 불러와야겠지
# 왜 쟤를 불러왔겠어 써야하니까지
# 클래스 - 변수(값 저장)와 메소드(동작) 두가지만 존재
class PostForm(forms.ModelForm):
    #forms에서 불러온 modelform을 쓰겠다
    #title = Post  XXXXX
    # 원래 필드담는건데 post 적으면 안되는거니까 - 그걸 meta에 적을게 이런거임
    # 어떠한 인풋을 어떠한 타입으로 정의하겟다를 원래 적었었는데
    class Meta: # 모델이랑 연결하려고
        # meta data 모델폼이 ㅓ떠한 정보를 가지고 있는지 알려주는 데이터
        model = Post # 그래서 바로 모델 쓰고 
        fields = ('__all__') # 필드 정의하고
        fields = ('title', 'content')


# 다 나열하는거 귀찮아서 form 쓰는데 기껏 쓰는데 어차피 또 같은 코드 적는거니까 ----- 모델이랑 연결시키자
# 그래서 모델폼 
```

