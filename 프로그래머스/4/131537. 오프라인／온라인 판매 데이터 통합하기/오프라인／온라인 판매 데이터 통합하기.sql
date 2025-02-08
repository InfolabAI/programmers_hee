select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT -- NOTE 틀린 부분. DATE_FORMET 뒤에는 항상 as 로 새 칼럼명 지정해줘야 함
from ONLINE_SALE
where SALES_DATE between '2022-03-01' and '2022-03-31'

union

select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT
from OFFLINE_SALE
where SALES_DATE between '2022-03-01' and '2022-03-31'

order by -- NOTE 틀린 부분. 한 번에 order by 하는 법.
    SALES_DATE,
    PRODUCT_ID,
    USER_ID












-- 250208
-- SELECT 
--     DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, -- DATE 의 포맷 변경
--     PRODUCT_ID,
--     USER_ID,
--     SALES_AMOUNT
-- FROM ONLINE_SALE
-- WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31' -- 조건 거는 법
-- 
-- UNION ALL -- 합치는 법
-- 
-- SELECT 
--     DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE,
--     PRODUCT_ID,
--     NULL AS USER_ID, -- 특정 열을 NULL 로 채우는 법
--     SALES_AMOUNT
-- FROM OFFLINE_SALE
-- WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
-- 
-- ORDER BY  -- 정렬하는 법
--     SALES_DATE ASC,
--     PRODUCT_ID ASC,
--     USER_ID ASC;