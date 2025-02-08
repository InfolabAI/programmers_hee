select ANIMAL_ID,	NAME
from animal_ins
where animal_type = 'Dog'
    and
    lower(name) like '%el%'
order by name














-- 250208
-- -- 코드를 입력하세요
-- SELECT ANIMAL_ID
--      , NAME
--   FROM ANIMAL_INS
--  WHERE ANIMAL_TYPE = 'Dog'          -- 개(Dog)만 조회
--    AND NAME IS NOT NULL             -- 이름이 NULL이 아닌 레코드만
--    AND LOWER(NAME) LIKE '%el%'      -- 이름에 "el"이 포함 (대소문자 구분X)
--  ORDER BY NAME;                     -- 이름 순 정렬