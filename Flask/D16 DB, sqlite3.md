# D16 DB, sqlite3

### csv 파일 읽기

### 1. hellodb.csv

```sqlite
(flask-venv) woonji:~/workspace $ sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> 
sqlite> .tables
examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;
id          first_name  last_name   age         country     phone        
----------  ----------  ----------  ----------  ----------  -------------
1           길동      홍         600         충청도   010-2424-1232
sqlite> .exit
```

### 2. tutorial.sqlite

```sqlite
(flask-venv) woonji:~/workspace $ sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .databases
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/tutorial.sqlite3                   
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT 
   ...> );
```

```sqlite
sqlite> .tables
classmates
sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT 
);
sqlite> DROP TABLE classmates; # 삭제
sqlite> .tables
```

### 3. 다음과 같은 스키마를 가지고 있는 classmate 테이블을 만들기

**colomn        datatype**

id                  INT

name           TEXT

age               INT

address       TEXT

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT
   ...> age INT
   ...> address TEXT
   ...> );
sqlite> .tables
classmates
sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT
age INT
address TEXT
);
```

만약 파일 읽을때

```sqlite
.read class_table.sql
```

class_table.sql

```sql
CREATE TABLE classmate (
id INT PRIMARY KEY,
name TEXT,
age INT,
address TEXT
);
```



### 4. 파일 추가하기 (insert.sql)

```sql
INSERT INTO classmate(name, age)
VALUES('홍길동', 23);
```

```sqlite
sqlite> .headers on
sqlite> .mode column
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
            홍길동   23                    
```



### 5. Data 추가 (INSERT)

classmates 테이블에 id가 2이고, 이름이 홍길동이고,나이가 30이고,  주소가 서울인 데이터 넣기.

```sql
INSERT INTO classmate --모든 data를 받을때는 column명 필요 없음
VALUES(2, '홍길동', 30, '서울');
```

```sqlite
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------                    
            홍길동   23                    
2           홍길동   30          서울    
```



### 6. Data 추가2

class_table.sql

```sql
CREATE TABLE classmate (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
```

* not null은 인자값 없으면 에러!

insert.sql

```sql
INSERT INTO classmate(name, age)
VALUES('안상현', 43);
INSERT INTO classmate(name, age)
VALUES('신채원', 15);
INSERT INTO classmate(name, age)
VALUES('박수현', 5);
```

```sqlite
sqlite> .read class_table.sql

sqlite> .read insert.sql
Error: near line 7: NOT NULL constraint failed: classmate.address
Error: near line 9: NOT NULL constraint failed: classmate.address
Error: near line 11: NOT NULL constraint failed: classmate.address
```

* address가 필수 값인데 안들어가 있기 때문에 에러가 뜬다. 

### 7. 특정 column 가져오기

```sql
-- 1. 테이블값 모두 가져오기
SELECT * FROM classmate;

-- 2. 테이블의 특정 컬럼만 가져오기
SELECT id, name FROM classmate;

-- 3. 젤 위에꺼 2개만 가져오기
-- (가져오는 ROW(레코드) 개수를 지정하기)
SELECT id, name FROM  classmate LIMIT 2;

-- 4. 가져오는 ROW(레코드)의 시작점 지정 
-- (위에서부터 몇 개만 가져오기)
SELECT * FROM classmate LIMIT 1 OFFSET 2;

-- 5. 특정한 값을 가진 ROW만 조회하기
SELECT * FROM classmate WHERE address='서울';
```

```sqlite
# 1
sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           dkstkdgus   43          대전    
2           신채원   15          서울    
3           안상현   43          대전    
4           신채원   15          서울

#2
sqlite> SELECT id, name FROM classmate;
id          name      
----------  ----------
1           dkstkdgus 
2           신채원 
3           안상현 
4           신채원 

#3
sqlite> SELECT id, name FROM  classmate LIMIT 2;
id          name      
----------  ----------
1           dkstkdgus 
2           신채원 

#4
sqlite> SELECT * FROM classmate LIMIT 1 OFFSET 2;
id          name        age         address   
----------  ----------  ----------  ----------
3           안상현   43          대전    

#5
sqlite> SELECT * FROM classmate WHERE address='서울';
id          name        age         address   
----------  ----------  ----------  ----------
2           신채원   15          서울    
4           신채원   15          서울 
```

```sqlite
#6
sqlite> SELECT name FROM classmate WHERE address='서울';
name 
----------
신채원 
신채원 
```



### 8. delete

delete.sql

```sql
-- 보통 값을 지울때는 유니크한 값인 id를 지운다
DELETE FROM classmate WHERE id=3;
```

```sqlite
sqlite> .read delete.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           dkstkdgus   43          대전    
2           신채원   15          서울    
4           신채원   15          서울    
```



### 9. ubdate

update.sql

```sql
UPDATE classmate
SET name='강예원', address='제주'
WHERE id=4;
```

```sqlite
sqlite> .read update.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           dkstkdgus   43          대전    
2           신채원   15          서울    
4           강예원   15          제주    
```



* 원자값은 하나만 가질 수 있기 때문에 and는 사용불가. or은 가능
* https://bini-079.tistory.com/36 (데이터베이스 용어 정리)

```sql
UPDATE classmate
SET name='박성주', address='제주'
WHERE id=4 or id=6;
```

```sqlite
sqlite> .read update.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           dkstkdgus   43          대전    
2           신채원   15          서울    
4           박성주   15          제주
```

