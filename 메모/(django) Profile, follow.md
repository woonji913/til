# (django) Profile, follow

190417

### 1. 프로필 CRUD

C - User가 가입되면 이미 생성됨

D - User가 지워지면 같이 지워짐

R - 출력

U - 프로필 작성/수정

> 우리가 해야 할 것은 R, U



### 2. Follow

user : user = N : N



User Extends(유저 확장) - AbstrackUser 이거가지고 너네가 user 커스텀해!



### 3. User

models > AbstractBaseUser > **AbstractUser** > User

* AbstractUser를 쓴다.

* 결국 User가 아닌 get_user_model()을 바라보고 있다.