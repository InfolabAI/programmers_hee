-- 코드를 입력하세요
SELECT PRODUCT_ID
     , PRODUCT_NAME
     , PRODUCT_CD
     , CATEGORY
     , PRICE
  FROM FOOD_PRODUCT
 WHERE PRICE = (
    -- (1) 이 서브쿼리는 FOOD_PRODUCT 테이블 전체에서 PRICE의 최댓값 한 개를 반환함
    --     즉, "가장 큰 값"이 단일 값(스칼라)으로 결과가 나옴
    SELECT MAX(PRICE) 
      FROM FOOD_PRODUCT
 )
 -- (2) PRICE = (위 서브쿼리 결과) : 
 --     만약 여러 행이 동일한 최고가를 갖고 있다면,
 --     서브쿼리는 '최고가'라는 단일 숫자를 반환하므로,
 --     그 '가격'과 동일한 행은 모두 조회됨.
;
