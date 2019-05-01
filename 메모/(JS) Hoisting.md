# (JS) Hoisting, Callback

### 1. let 블록 스코프 예제

```javascript
{
    let x = '정운지'
    console.log(x) // 정운지
    {
        let x = 1
        console.log(x) //1
    }
    console.log(x) // 정운지
}
console.log(typeof x) // undefined
```

* 전역 변수의 오염



### 2. 변수 선언

* var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.

* let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.

* 선언되지 않은 변수(에러 o) !== undefined 변수(에러 x)

```javascript
let foo // undefined
let bar = undefined // undefined
baz // ReferenceError
```



```javascript
x 
var x = 1
x
> 1
```

*원래대로면 에러가 떠야하는데 안뜬다. 그게 var의 문제* 

```javascript
// JS 가 이해한 코드
var x
x  // undefined
x=1 // 1
x // 1
```



```javascript
if (x !== 1) {
    console.log(y)  // undefined
    var y = 3
    if (y === 3) {
        var x = 1
    }
    console.log(y) // 3
}
if (x === 1) {
    console.log(y) // 3
}
```



#### var로 변수를 선언하면 JS는 같은 변수를 여러번 정의 하더라도 무시한다.

```javascript
var x = 1
if (x === 1) {
    var x = 2
    console.log(x)  // 2
}
console.log(x)     // 2
```



### 3. 함수 호이스팅

* ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태

```javascript
ssafy()

function ssafy() {
    console.log('hoisting!')
} // 호출됨

let ssafy = function () {
    console.log('hoisting!!')
} // hoisting되지 않음
```

* ssafy() 명시적 호출



### 4. Callback 함수

* 콜백 함수는 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수.
* 함수를 명시적으로 호출하는게 아니라, 특정 이벤트가 발생 했을 때, 시스템에 의해 호출되는 함수.
* 일급객체
  * 일급객체의 3가지 조건
    1. 변수에 담을 수 있어야 한다.
    2. 인자로 전달할 수 있다.
    3. 반환 값(return value)으로 전달할 수 있다.

```javascript
// 일급 객체 3가지 조건
        const fco = function () { //1.
            return n => n + 1 //3. return value가 익명함수
        }
        console.log(fco) //2. fco가 console.log()함수의 인자로 전달됨.
```
```javascript
// 도전 num_101에 101을 담아야 한다.
        const num_101 = fco()(100)
        console.log(num_101)
```


* `setTimeout(callback, ms(time))`

```javascript
setTimeout(function () {
            console.log('3초 후 출력된다.')
        }, 3000)
// 한줄로! setTimeout(() => console.log('3초 후 출력된다.'), 3000)
```

* 동기(직렬) / 비동기(병렬)
  * 중간에 로드가 오래걸리는 함수
  
  * 비동기
  
  * 브라우저는 멀티 스레드?
  
  * 멀티스레드 N개?
  
    -> 스레드 1개를 동기가 아니라 비동기로 만들자!

* 비동기 처리 모델

  * block

    ```python
    from time import sleep
    
    def sleep_3s():
        sleep(3)
        print('Wake up!')
    
    print('start sleeping')
    sleep_3s() # blocking
    print('end of program') # 3초 기다렸다가 나온다.
    ```

  * non-block

    ```javascript
    const nothing = () => {}
    
    console.log('start sleeping')
    setTimeout(nothing, 3000) // non-block
    console.log('end of program') // 글자는 바로 나오고 3초뒤에 끝난다.
    ```

  * python code처럼 동작하게 하려면?

    ```javascript
    const logEnd = () => {
        console.log('end of program')
    }
    console.log('start sleeping')
    setTimeout(logEnd, 3000)
    ```

    

    `axios` `Ajax`

    좋아요 댓글 팔로우 리다이렉트 되는 것을 없앨 것임.

    

#### * non-blocking

해당 함수의 시작 이후 종료될 때까지 기다리지 않고 바로 다음 줄의 코드를 실행하는 것을 의미.

코드의 실행을 막지 않는다.

```javascript
function first() {

    console.log('first')
}
function second() {

    console.log('second')
}
function third() {

    console.log('third')
}

first()
// second()
// setTimeout(second, 1000)
setTimeout(second, 0)
third()
```

```bash
$ node non_blocking
first
third
second
```

> 0초여도 callback함수에 한번 들어갔다 나오기 때문에 순서가 밀린다.

#### * 이벤트 루프

시간의 흐름에 따라 코드의 수행을 처리, 그때마다 JS 엔진을 작동 시킴.



### 4. EventListener

[무엇]을 [언제] [어떻게] 한다.

버튼을 클릭하면(이벤트) 뿅한다.(리턴)

```javascript
// 1. 무엇 => 버튼
const button = document.querySelector('#this-button')

// 2. 언제 => 버튼을 `클릭`하면
button.addEventListener('click', event => {
     const area = document.querySelector('#my')
     // 3. 어떻게 => 뿅
     area.innerHTML = '<h1>뿅</h1>'
    })
```

