# 0410_Workshop

데이터베이스에 값을 추가할 때, 아래와 같이 검증하려고 한다. 적절한 코드를 작성하시오.

![image](https://user-images.githubusercontent.com/46305540/56705407-b8136e00-674b-11e9-9963-042b673510ad.png)

![image](https://user-images.githubusercontent.com/46305540/56705416-c82b4d80-674b-11e9-9e7e-ce9e496d1d5d.png)



```python
from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100,
                                validators = [EmailValidator(message='이메일 형식에 맞지 않습니다.')])
                                
    age = models.IntegerField(validators =[MinValueValidator(limit_value=20, message='미성년자는 노노')] )
```


