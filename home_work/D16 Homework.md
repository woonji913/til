# D16 Homework

1. 테이블 생성

```sql
CREATE TABLE friends (
id INTEGER PRIMARY KEY,
name TEXT,
location TEXT
);
```

2. 데이터 입력

```sql
INSERT INTO friends VALUES (1, 'Justin', 'Seoul');
INSERT INTO friends VALUES (2, 'Simon', 'New York');
INSERT INTO friends VALUES (3, 'Chang', 'Las Vegas');
INSERT INTO friends VALUES (4, 'John', 'Sydney');
```

3. 스키마 변경

```sql
--ALTER TABLE
--1. Rename Table
--2. Add new column to Table

ALTER TABLE friends ADD CLOLUMN married INTEGER
--ALTER TABLE friends
--RENAME RO new_table_name
```

4. 데이터 추가

```sql
UPDATE friends SET location='LA', married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE ID=2;
UPDATE friends SET married=0 WHERE ID=3;
UPDATE friends SET married=1 WHERE ID=4;
```

5. 특정 데이터 삭제

```SQL
DELETE FROM friends WHERE married=0;
```

6. 테이블 삭제

```SQL
DROP TABLE friends
```

