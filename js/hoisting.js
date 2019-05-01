// let 블록 스코프 예제
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
// 전역 변수의 오염

//  var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.
//  let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.
//  선언되지 않은 변수(에러 o) !== undefined 변수(에러 x)

let foo // undefined
let bar = undefined // undefined
baz // ReferenceError

/*
x 
var x = 1
x
> 1
원래대로면 에러가 떠야하는데 안뜬다. 그게 var의 문제 

JS 가 이해한 코드
var x
x  // undefined
x=1 // 1
x // 1
*/

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

// var로 변수를 선언하면 JS는 같은 변수를 여러번 정의 하더라도 무시한다.
var x = 1
if (x === 1) {
    var x = 2
    console.log(x)  // 2
}
console.log(x)     // 2

// 함수 호이스팅
// ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태
ssafy()

// function ssafy() {
//     console.log('hoisting!')
// }

let ssafy = function () {
    console.log('hoisting!!')
} // hoisting되지 않음