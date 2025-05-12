  """
  출처:프로그래머스,
  https://school.programmers.co.kr/learn/courses/30/lessons/299308
  """
  
  # 풀이 과정
  """
  select
    QUARTER, count(QUARTER) "ECOLI_COUNT"
    # case 
    #     when month(DIFFERENTIATION_DATE) <=3 then "1Q"
    #     when 3< month(DIFFERENTIATION_DATE)<=6 then "2Q"
    #     when 6< month(DIFFERENTIATION_DATE)<=9 then "3Q"
    #     else "Q4"
    # end as QUARTER
from (select 
        case 
        when month(DIFFERENTIATION_DATE) <=3 then "1Q"
        when month(DIFFERENTIATION_DATE) > 3 and  month(DIFFERENTIATION_DATE) <= 6 then "2Q"
        when month(DIFFERENTIATION_DATE) > 6 and  month(DIFFERENTIATION_DATE) <= 9 then "3Q"
        else "4Q"
        end as QUARTER
      from ECOLI_DATA) as A
group by QUARTER
order by QUARTER asc
  """
  
  #풀이 과정_개선 중 
  """
  select
    QUARTER, count(QUARTER) "ECOLI_COUNT"
    # case 
    #     when month(DIFFERENTIATION_DATE) <=3 then "1Q"
    #     when 3< month(DIFFERENTIATION_DATE)<=6 then "2Q"
    #     when 6< month(DIFFERENTIATION_DATE)<=9 then "3Q"
    #     else "Q4"
    # end as QUARTER
from (select 
        case 
        when month(DIFFERENTIATION_DATE) <=3 then "1Q"
        when month(DIFFERENTIATION_DATE) > 3 and  month(DIFFERENTIATION_DATE) <= 6 then "2Q"
        when month(DIFFERENTIATION_DATE) > 6 and  month(DIFFERENTIATION_DATE) <= 9 then "3Q"
        else "4Q"
        end as QUARTER
      from ECOLI_DATA) as A
group by QUARTER
  """