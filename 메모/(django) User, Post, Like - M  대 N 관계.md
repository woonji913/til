# (django) User, Post, Like - M  대 N 관계

1. 관계 설명

```
user는 여러 post에 like 할 수 있고,

post는 여러 user로부터 like 받을 수 있다.
```

* 중개모델(조인테이블)이 조인 테이블을 따로 생성해서 관계를 설정하는게 M:N



2. 복수형/소스모델과 타겟모델

```
소스모델 : MTM 필드가 있는 모델 (환자)

타겟모델 :  MTM 필드가 없는 모델(의사)
```

**역참조** : 타겟모델이 소스모델을 참조



3. User(타겟) : Post(소스)

* 1 : N

(소스에서 타겟을 참조)

```python
post = Post.objects.get(pk=1)
post.user 
```

(타겟에서 소스를 역참조)

```python
user = User.objects.get(pk=1)
user.post_set.all()
```

* M : N

```python
post = Post.objrcts.get(pk=1)
post.user
post.like_users.all()  # 참조
```

```python
user.post_set.all() # 오류가 난다.
>> 유저가 작성한 글들인지 유저가 좋아요한 글들인지 모른다.(역참조 에러)
>> related_name='like_posts' 설정을 해줘야함.
```

```python
user.post_set.all() # 내가 작성한 글들
user.like_posts.all() # 내가 좋아요한 글들
```

