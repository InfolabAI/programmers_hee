-- 코드를 입력하세요
-- ANIMAL_INS 테이블에서 보호 시작 시각(DATETIME) 컬럼 중 가장 작은 값(가장 먼저 들어온 시각)을 반환
SELECT MIN(DATETIME) AS 시간
  FROM ANIMAL_INS;


-- ANIMAL_INS 테이블을 DATETIME 기준 오름차순으로 정렬한 뒤, 가장 위의 한 건만 조회
-- SELECT DATETIME AS 시간
--   FROM ANIMAL_INS
--  ORDER BY DATETIME
--  LIMIT 1;
