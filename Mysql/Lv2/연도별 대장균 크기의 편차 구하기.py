  """
  출처:프로그래머스,
  https://school.programmers.co.kr/learn/courses/30/lessons/299310
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