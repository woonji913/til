# 0411_Homework

1번. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를 사용한다. 해당 파일은 기본적으로 각각의 app에 fixtures 폴더에 있어야하며, 파일 형식은 [            ]이거나 [           ]이다.



`json` , `yaml`



2번. 워크샵처럼 실제 Django에 데이터가 저장되어 있을 때, 아래의 fixtures 파일을 만들고자 한다. 사용해야하는 명령어를 작성하라.

```yaml
- model: myapp.person
  pk: 1
  fields:
    first_name: John
    last_name: Lennon
- model: myapp.person
  pk: 2
  fields:
    first_name: Paul
    last_name: McCartney
```

1) `pip install pyyaml`

2) `python manage.py dumpdata myapp.person --format yaml > final.yaml`