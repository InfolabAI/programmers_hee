-- 코드를 입력하세요
SELECT B.BOOK_ID
     , A.AUTHOR_NAME
     , DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE  -- (1) 시·분·초를 제거하고 yyyy-mm-dd 형태로 표시
     
  FROM BOOK AS B
       JOIN AUTHOR AS A
         ON B.AUTHOR_ID = A.AUTHOR_ID                                -- (2) 책(BOOK)의 저자ID와 저자 테이블(AUTHOR)의 저자ID를 매칭
 WHERE B.CATEGORY = '경제'                                           -- (3) "경제" 카테고리만 필터링
 ORDER BY B.PUBLISHED_DATE;                                          -- (4) 출판일 오름차순으로 정렬 (가장 이른 출판일부터)