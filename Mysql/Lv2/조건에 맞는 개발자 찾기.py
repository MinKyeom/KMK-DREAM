"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/276034  
"""
"""
-- 파이썬과 c# 스킬을 포함한 조합 구성 확보 후 테이블 조인 생각
# select ID,EMAIL,FIRST_NAME,LAST_NAME
-- 이진법 구성을 보면 이진법 & 처리 생각!
select distinct A.ID,A.EMAIL,A.FIRST_NAME,A.LAST_NAME
from DEVELOPERS as A, 
    (select *
    from SKILLCODES 
    where NAME in ('Python','C#')) as B
where A.SKILL_CODE & B.CODE = B.CODE
order By A.ID asc
"""

# 풀이과정_개선 중

"""
문제점: mysql에서는 grouping sets를 지원하지 않는다
-- 파이썬과 c# 스킬을 포함한 조합 구성 확보 후 테이블 조인 생각
# select ID,EMAIL,FIRST_NAME,LAST_NAME
# from 

select *
from DEVELOPERS
group by 
    grouping sets (
    (NAME)
    )
"""