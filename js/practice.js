var _ = require('lodash');

// 메뉴 랜덤 픽
let list = ['짜장면', '짬뽕', '볶음밥',]
let pick = _.sample(list)
let menu = {
    짜장면: 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2017/0427/IE002151398_STD.JPG',
    짬뽕: 'https://t1.daumcdn.net/cfile/tistory/192F441E49DB7D5E0A',
    볶음밥:'https://craftlog.com/m/i/6115186=s1280=h960',
}
console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])

// 로또
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)
console.log(`행운의 번호: ${lottery}`)

// 최솟값 구하기
let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}

let getMinFromArray = nums => {
    let min = Infinity // 양의 무한대, -Infinity: 음의 무한대
    // nums 배열을 돌면서 min 변수와 비교하여 최소 값을 찾는다.
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1, 2, 3, 4, 5, 6, 7,]
console.log(getMinFromArray(ssafy))