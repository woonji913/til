# D04 Homework

## 1번

 Python에서 사용할 수 없는 식별자(예약어)를 찾아 3개만 작성하세요.

```
False, None, True
```



## 2번

파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

a = 0.1 * 3

b = 0.3

```python
abs(a - b) <= 1e-10
>>> True
```

## 3번

“ 안녕, 철수야 ” 를 String Interpolation을 사용하여 출력하세요.

```python
name = "철수"
ptint(f'"안녕, \"{name}\"야"')
>>> "안녕, 철수야"
```

## 4번

다음 중 형변환시 오류가 발생하는 것은?

1) str(1)      2) int(‘30’)       3) int(5)       4) bool(‘50’)           **5) int(‘3.5’)**



## 5번

변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.

String, List, Tuple, Range, Set, Dictionary



mutable: list,  range, set, dictionary

immutable: string, tuple