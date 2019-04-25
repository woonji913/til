# 0411_Workshop

아래는 Django에서 myapp의 Musician class에 저장된 기본 시드 데이터이다. 이를 적용하기 위해 필요한 json 파일을 만들어 적용해보자.

1. models.py

```python
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
```

2. admin.py

```python
from django.contrib import admin
from .models import *
# Register your models here.

class MusicianAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name',]
admin.site.register(Person, MusicianAdmin)
```

3. (폴더) fixtures > (파일) sample.json

```json
[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

