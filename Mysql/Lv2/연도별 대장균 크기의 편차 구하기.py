  """
  출처:프로그래머스,
  https://school.programmers.co.kr/learn/courses/30/lessons/299310
  """
  # 풀이 과정
  """
  -- 전체 생각: sql문 구성 시 불러오는 순서 생각 후 구성
-- 부모 개체가 전년도 개체일 것인거 생각
-- group by 사용시 select문에서 group by 관련되지 않은 컬럼은 포함 불가이다.
select year(A.DIFFERENTIATION_DATE) "YEAR",(B.check- A.SIZE_OF_COLONY) as "YEAR_DEV",A.ID
-- join 방식 및 구성 방식 고민 후 > 작성 
-- 직전 부모 개체를 파악하는 테이블 합성 > 크로스 조인?
-- 연도별 그룹 묶는거로 인해 크로스 조인 오류 가능성 발생
-- 조인 방법 생각해보기 
from ECOLI_DATA A,
    (select max(SIZE_OF_COLONY) "check",year(DIFFERENTIATION_DATE) "y"
        from ECOLI_DATA
        group by year(DIFFERENTIATION_DATE) ) as B
where year(A.DIFFERENTIATION_DATE)= B.y
-- 연도별 최고 무게 대장균과 지금 현재 무게의 편차를 구하기
# where A.PARENT_ID=B.ID
-- 연도별? > 연도를 묶는 Group by Having 절 생각
order by year(A.DIFFERENTIATION_DATE) asc,YEAR_DEV asc
  """
  
  # 풀이과정_개선 중 
  """
  -- 전체 생각: sql문 구성 시 불러오는 순서 생각 후 구성
  -- 부모 개체가 전년도 개체일 것인거 생각
select YEAR,YEAR_DEV,A.ID
  -- join 방식 및 구성 방식 고민 후 > 작성 
  -- 직전 부모 개체를 파악하는 테이블 합성 > 크로스 조인?
  -- 연도별 그룹 묶는거로 인해 크로스 조인 오류 가능성 발생
  -- 조인 방법 생각해보기 
from ECOLI_DATA A,ECOLI_DATA B
where A.PARENT_ID=B.ID
  -- 연도별? > 연도를 묶는 Group by Having 절 생각
order by YEAR asc
  """
  
  # 다른 사람 풀이 
  """_
  SELECT   YEAR(A.DIFFERENTIATION_DATE) AS YEAR
                  , ABS(A.SIZE_OF_COLONY - B.MAX_SIZE) AS YEAR_DEV
                  , A.ID
     LEFT
     JOIN  (
                 SELECT   YEAR(A.DIFFERENTIATION_DATE) AS YEAR
                                  , MAX(A.SIZE_OF_COLONY) AS MAX_SIZE
                    FROM   ECOLI_DATA A
                 GROUP  
                          BY   YEAR(A.DIFFERENTIATION_DATE)
                 ) B
          ON  YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
 ORDER
          BY   YEAR ASC
                  , YEAR_DEV ASC
  """