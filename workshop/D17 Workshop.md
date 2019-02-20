# D17 Workshop

문제)

자신의 반에 있는 사람들의 데이터를 저장하는 Student모델을 생성합니다.
Student모델이 가져야 할 필드는 아래와 같습니다.



name(이름) : CharField
email(이메일) : CharField
birthday(생년월일) : DateField
age(나이) : IntegerField

```python
from django.db import models

class Student(models.Model):  
    name = models.CharField(max_length=10) 
    email = models.CharField(max_length=25)
    birthday = models.DateTimeField()  
    age = models.IntegerField()
```

모델 마이그레이션 작업을 거친 후 Admin페이지에서 주변 학생들의 이름을 세명 저장합니다.

```bash
python manage.py makemigrations student
python manage.py migrate

person = Student(name='정운지')
person.save()
person = Student(name='김준석')
person.save()
person = Student(name='김호영')
person.save()
```



저장 후 Admin페이지에서 학생들의 목록을 보기 쉽게 만들기 위해서 `__str__`메소드를 오버라이드 하여 name이 출력되게 만듭니다.



```python
class Student(models.Model):  

	def __str__(self):
    	return f"{self.name}"
```



