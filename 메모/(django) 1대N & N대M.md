# Django 1:N & N:M

190416 화요일

### 1. One to Many

1. models.py 설정

```python
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
```

user 1 : post N

post 1 : comment N



2. 정보 입력

```python
user1 = User.objects.create(name='kim')
user2 = User.objects.create(name='lee')
post1 = Post.objects.create(title='1글', user=user1)
post2 = Post.objects.create(title='2글', user=user1)
post3 = Post.objects.create(title='3글', user=user2)
c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
c7 = Comment.objects.create(content='!2글2댓글', user=user2, post=post2)
```



3. 정보 불러오기

* 1번 사람이 작성한 게시글은?
```python
user1.post_set.all()
```
* 1번 사람의 게시글별로 댓글을 출력해보세요.
```python
for post in user1.post_set.all():
    for comment in post.comment_set.all():
        print(comment.content)
```
* 2번 댓글을 쓴 사람은?
```python
c2.user
```
* 2번 댓글을 쓴 사람의 게시글들은?
```python
  c2.user.post_set.all()
```
* 1번 글의 첫번째 댓글을 작성한 사람의 이름은?
```python
  post1.comment_set.first().user.name
  post1.comment_set.all()[0].user.name
```
* 1번 글의 2번째부터 4번째까지의 댓글을 가져오세요.
```python
  post1.comment_set.all()[1:4]
```
* 1번 글의 2번째 댓글을 작성한 사람의 첫번째 게시글 작성자의 이름은?
```python
  post1.comment_set.all()[1].user.post_set.first().user.name
```
* 1번 댓글의 user 정보만 가져온다면?
```python
  c = Comment.objects.values('user').get(pk=1)
```
ex) 댓글이 아주 많을 때 (댓글 1억개)
```python
c = Comment.objects.all().values('user')
```
* 2번 유저가 작성한 댓글을 content의 내림차순으로 가져오면?
```python
user2.comment_set.order_by('-content')
```
* '1글'이라는 제목인 게시글들을 가져오세요.
```python
Post.objects.filter(title='1글')
```
* 제목에 '글'이라는 단어가 있는 게시글은?
```python
Post.objects.filter(title__contains='글')
```
* 댓글 중에 해당 글의 제목에 1이 포함된 댓글은?
```python
Comment.objects.filter(post__title__contains='1')
```



### 2. Many to Many

1. models.py 설정

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    
    def __str__(self):
        return self.name
        
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

다 대 다의 경우 중개모델이 필요하다.

여기서는 reservation



* `Reservation`을 통해서(through) 가지고 오겠다.

```python
doctors = models.ManyToManyField(Doctor, through='Reservation')
```



2. 정보 입력

```python
doctor = Doctor.objects.create(name='kim')  
patient = Patient.objects.create(name='john')
Reservation.objects.create(doctor=doctor, patient=patient)
```

* 의사 입장에서 모든 예약 불러오기
```python
doctor.reservation_set.all()
>> <QuerySet [<Reservation: Reservation object (1)>]>
```
* 환자 입장에서 모든 예약 불러오기
```python
patient.reservation_set.all() 

>> <QuerySet [<Reservation: Reservation object (1)>]>
```



> 추가정보 입력(환자 추가)

```python
patient2 = Patient.objects.create(name='Tom') 
Reservation.objects.create(doctor=doctor, patient=patient2)
```



* 의사 입장에서 모든 예약 불러오기
```python
doctor.reservation_set.all()

>> <QuerySet [<Reservation: Reservation object (1)>, <Reservation: Reservation object (2)>]>
```
* 의사의 모든 예약환자 이름 출력
```python
for reservation in doctor.reservation_set.all():
    print(reservation.patient.name)

>> john
>> Tom
```



3. doctors 컬럼 만든 후 정보 불러오기

> 추가정보 입력(의사 추가)

```python
doctor = Doctor.objects.create(name='park') 
Reservation.objects.create(doctor=doctor, patient=patient) 
# 여기서 doctor는 'park'이고 patient는 'john'
```




* 의사('park')의 모든 환자 불러오기

```python
doctor.patient_set.all()

>> <QuerySet [<Patient: john>]>
```



4. 역참조

#### * 역참조하기

```python
related_name='patients'
```

models.py 

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    
    def __str__(self):
        return self.name
        
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



* 의사('kim')의 모든 환자 불러오기

```python
doctor.patients.all()

>> <QuerySet [<Patient: john>, <Patient: Tom>]>
```



##### * 이제 이후로는 `patient_set.all()`은 사용 못한다. (django가 이미 `patients(역참조)`를 쓰기로 정했기 때문에.)



### * 역참조 이후

models.py 최종

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    
    def __str__(self):
        return self.name
```

`manytomany_patient_doctors `가 자동으로 만들어진 꼴이 되어서 중개 모델이 필요 없게 된다.



정보 추가 (마이그레이션을 다시 하기 때문에 정보 다시 입력)

```python
doctor = Doctor.objects.create(name='kim')
patient = Patient.objects.create(name='john')
```



* 의사에게 환자 추가

```python
doctor.patients.add(patient)
```

* 의사의 환자 확인

```python
doctor.patients.all()

>> <QuerySet [<Patient: john>]>
```

* 환자 삭제

```python
doctor.patients.remove(patient)
```



