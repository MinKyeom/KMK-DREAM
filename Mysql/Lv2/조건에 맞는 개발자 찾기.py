"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/276034  
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