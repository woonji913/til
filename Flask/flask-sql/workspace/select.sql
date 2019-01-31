-- 테이블값 모두 가져오기
SELECT * FROM classmate;

-- 테이블의 특정 컬럼만 가져오기
SELECT id, name FROM classmate;

-- 젤 위에꺼 2개만 가져오기
-- (가져오는 ROW(레코드) 개수를 지정하기)
SELECT id, name FROM  classmate LIMIT 2;