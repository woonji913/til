// 1. forEach
// 2. forEach 함수는 아무것도 return 하지 않는다.

// ES5
var colors = ['red', 'blue', 'green',]

for (var i = 0; i < colors.length; i++) {
    console.log(colors[i])
}

// ES6+
const COLORS = ['red', 'blue', 'green',]
COLORS.forEach(color => console.log(color))

// exercise 1-1 아래 함수에 for를 forEach로 바꾸시오.
function handlePosts() {
    const posts = [
        {id: 23, title: 'daily news'},
        {id: 52, title: 'Code City'},
        {id: 105, title: 'The Ruby'},
    ]

    // for (let i = 0; i < posts.length; i++) {
    //     savePosts(post)
    // }
    posts.forEach(post => savePosts())
}

// exercise 1-2 아래 코드의 images 배열안에 있는 정보(height, width)를 곱해 
// 넓이를 구하여 areas 배열에 저장하는 코드를 forEach 헬퍼를 사용해 작성해보자.
const images = [
    {height: 10, width: 30},
    {height: 20, width: 90},
    {height:54, width:32},
]
const areas = []
images.forEach(image => areas.push(image.height * image.width))
console.log(areas)

// 2. MAP
// map 함수는 새로운 배열을 return한다. (배열 요소를 변형)
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때.
// map filter는 모두 사본을 return하며 원본 배열은 바뀌지 않는다.

const NUMBERS = [1, 2, 3,]

const DOUBLE_NUMBERS = NUMBERS.map(function (number) {
    return number * 2
})
// const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2) // 한줄로
console.log(DOUBLE_NUMBERS)

// exercise 2-1 map 헬퍼를 사용해, images 배열 안의 Object 들만 저장되어 있는 height 배열에 저장해보자.
const IMAGES = [
    {height: '34px', width: '39px'},
    {height: '54px', width: '19px'},
    {height:'83px', width:'75px'},
]
const heights = IMAGES.map(image => image.height)
console.log(heights)

// exercise 2-2 map 헬퍼를 사용해, (distance / time) 을 저장하는 배열 speeds를 만들어보자.
const trips = [
    {distance: 34, time: 10},
    {distance: 90, time: 20},
    {distance: 59, time: 25},
]
const speeds = trips.map(trip => (trip.distance / trip.time))
console.log(speeds)

// exercise 2-3 다음 두 배열을 객체로 결합한 comics 배열을 만들어보자. 
// 힌트 : enumerate
const brands = ["Marvel", "DC",]
const movies = ["IronMan", "BatMan",]
const comics = brands.map((x, i) => ({name: x, hero: movies[i]}))
console.log(comics)

// (brands 요소가 key, movies 요소가 value)
const comics2 = {}
brands.map((brand, i) => comics2[brand] = movies[i])
console.log(comics2)

// 3. filter
// filter 함수는 필터링된 요소들만 배열로 return한다.
// 배열에서 필요한 것들만 남길 때 사용한다.
const PRODUCTS = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
 ]

 const fruitProducts = PRODUCTS.filter(function (product) {
     return product.type === 'fruit'
     // 해당 조건문에서 true를 만족할 경우 return
 })
//  const fruitProducts = PRODUCTS.filter(product => product.type === 'fruit')
 console.log(fruitProducts)

 // exercise 3-1 filter 헬퍼를 사용해서, numbers 배열중 50보다 큰 값들만 필터링해서 filteredNumbers에 저장하라.
 const numbers2 = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

const filteredNumbers = numbers2.filter(num => num > 50)
console.log(filteredNumbers)

// 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.
const users = [
    {id: 1, admin: true},
    {id: 2, admin: false},
    {id: 3, admin: false},
    {id: 4, admin: false},
    {id: 5, admin: true},
]

const filteredUsers = users.filter(user => user.admin === true)
console.log(filteredUsers)