-- 코드를 입력하세요
SELECT AI.NAME
     , AI.DATETIME
  FROM ANIMAL_INS AS AI
  LEFT JOIN ANIMAL_OUTS AS AO 
         ON AI.ANIMAL_ID = AO.ANIMAL_ID
 WHERE AO.ANIMAL_ID IS NULL           -- (1) 입양 기록이 없는 동물(입양 못 간 동물)
 ORDER BY AI.DATETIME                 -- (2) 가장 오래 보호소에 있던(입소일이 가장 빠른 순)
 LIMIT 3;                             -- (3) 3마리만 조회
