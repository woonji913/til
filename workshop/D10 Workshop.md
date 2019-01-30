# D09 Workshop



##### CSS

nth-child(n)

* 모든 자식의 순서에서 찾음
* 해당하는 태그의 순서



nth-of-type(n)

* 해당하는 자식 태그 요소에서 순서를 찾음
* 부모 속성에서 특정태그를 가진 자식 속성에서 몇번째에 해당하는지



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        #ssafy > p:nth-child(2) {
            color: red;
        }
        #ssafy > p:nth-of-type(2) {
            color: blue;
        }
    </style>
</head>
<body>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</body>
</html>
```