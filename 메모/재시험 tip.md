# 재시험 tip

minsu [5:40 PM]
- **메소드 다 돌려보고 출력값 보기 :  반환되는지 None인지** << **제일 중요!!**
 - **리스트, 딕셔너리 필수!**
- 모든 자료형 시퀀스, 뮤터블 여부 구분하기
 - a = ('t')  #string, 하나 요소가 튜플되려면 쉼표 있어야함 a = ('t',)
- -5~256은 미리 캐싱 되어있기 때문에 항상 True
- 

  ```이중 딕셔너리 리스트
  my_dict = {'inner':{}} 여기에 키 밸류 넣으려면?
  my_dict['inner']['a'] = value
  ```


- 인덱싱, 슬라이싱 개념 다시 복습

- 리스트 딕셔너리 컴프리헨션 읽을 줄 알기

- string은 find, replace 위주로 보기

- 조건문/반복문 출력값 확인하기! 마지막 변수명 주의

- map, reversed 리턴값은 그냥 객체로 출력됨! 확인하기

- 다인자 순서 유의하기 : return a, c, b 이런 것

 - **위치 인자, 키워드 인자, *, ** 개념 정리**

- deepcopy 시험 문제 보기마다 파이썬 튜터로 확인하기

- OOP 개념 정리

 - 인스턴스, 클래스 변수 어떤 게 출력되는지

```iu = Person()
    iu.greeting() == Person.greeting('iu') << 인스턴스 self자리에 iu가 들어간 것
```



- **end=', ' << 띄어쓰기 된 상태로 출력됨. 대충 보지 않기.**


```python
>>> def func(*numbers):
	for number in numbers:
		if number % 5:
			print(number, end=', ')
		else:
			return number

		
>>> print(func(1, 3, 5, 7))
1, 3, 5
```

