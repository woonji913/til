--1.
SELECT SUM(누적관객수) FROM movies;
--2.
SELECT 영화이름, MAX(누적관객수) FROM movies;
--3.
SELECT 장르, MIN(상영시간) FROM movies;
--4. 
SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
--5.
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';
--6. 
SELECT COUNT(*) FROM movies WHERE 상영시간>=100 and 장르='애니메이션';

