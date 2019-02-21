# D18 Homework

20190221

1. Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공격은 무엇을 의미 하는가?

```
사이트 간 요청 위조 ( CSRF, Cross-site request forgery )
사용자가 " 자신의 의지와는 무관하게 " 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는 공격을 말합니다.
XSS 공격은 사용자가 특정 웹사이트를 신용하는 점을 노린 것이라면, CSRF 공격은 특정 웹사이트가 사용자의 웹 브라우저를 신용하는 상태를 노린 것이라는 점에서 차이가 있습니다.

일단 사용자가 웹사이트에 로그인한 상태에서 공격자가 심어 놓은 CSRF 공격 코드가 삽입된 페이지를 열면, 공격 대상이 되는 웹사이트는 믿을 수 있는 사용자로부터 요청된 것으로 판단하게 되어 공격에 노출 됩니다.

ex)
만일, A라는 사이트의 사용자 개인 비밀번호 변경을 하는 주소 패턴이 'abc.com/user.do?cmd=user_passwd_change&user=admin&newPwd=1234'라고 할 때, 이러한 링크를 XSS 공격으로 사용자에게 메일로 보낸 뒤, 사용자가 메일을 읽게되면 해당 사용자의 패스워드가 1234로 변경됩니다.
```



2. 기본적으로 Django에서 views.py에 함수들을 정의할 때 request인자 값을 넣어주어야 한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요.

![1550728093377](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550728093377.png)

```python
title = request.POST.get('title')
```



3. 다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit페이지를 위한 views.py의 코드이다.

![1550728183653](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550728183653.png)

아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요

![1550728233234](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550728233234.png)



```html
<form action="/posts/{{post.id}}/update/" method="post">
	{% csrf_token %}
    <input type="text" name="title" value="{{ post.title }}"/>
    <input type="text" name="content" value="{{ post.content }}"/>
    <input type="submit" value="submit"/>
</form>  
```

