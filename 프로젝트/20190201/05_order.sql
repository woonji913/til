--1.
SELECT * FROM movies WHERE ORDER BY 누적관객수 DESC LIMIT 5;
--2.
SELECT * FROM movies WHERE 장르='애니메이션'\ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;
--3. 
SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;