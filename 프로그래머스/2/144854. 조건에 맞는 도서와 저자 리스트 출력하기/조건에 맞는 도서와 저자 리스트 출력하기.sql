select BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK as B join AUTHOR as A -- NOTE 틀린 부분. join A and B 가 아니라, A join B 로 작성해야 함
    on B.AUTHOR_ID = A.AUTHOR_ID -- NOTE 틀린 부분. == 가 아니라 = 임
where CATEGORY = '경제'
order by PUBLISHED_DATE; -- NOTE 틀린 부분. '컬럼명' 이 아니라, 그냥 컬럼명을 써야 함















--  250208
-- -- 코드를 입력하세요
-- SELECT B.BOOK_ID
--      , A.AUTHOR_NAME
--      , DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE  -- (1) 시·분·초를 제거하고 yyyy-mm-dd 형태로 표시
--      
--   FROM BOOK AS B
--        JOIN AUTHOR AS A
--          ON B.AUTHOR_ID = A.AUTHOR_ID                                -- (2) 책(BOOK)의 저자ID와 저자 테이블(AUTHOR)의 저자ID를 매칭
--  WHERE B.CATEGORY = '경제'                                           -- (3) "경제" 카테고리만 필터링
--  ORDER BY B.PUBLISHED_DATE;                                          -- (4) 출판일 오름차순으로 정렬 (가장 이른 출판일부터)