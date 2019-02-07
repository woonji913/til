# D16 Workshop

1. 컬럼추가

```sql
ALTER TABLE bands ADD COLUMN members INTEGER;
```

2.  테이블 수정하기

```SQL
UPDATE bands SET memder=4 WHERE id=1;
UPDATE bands SET memder=5 WHERE id=2;
UPDATE bands SET memder=9 WHERE id=3;
```

3. id가 3인 레코드의 멤버를 5로 수정

```SQL
UPDATE bands SET member=5 WHERE id=3;
```

4. id가 2인 레코드 삭제

```SQL
DELETE FROM bands WHERE id=2;
```

