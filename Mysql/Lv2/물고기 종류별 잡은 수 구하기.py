"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/293257
"""

# 풀이 과정 
"""
select count(B.FISH_NAME) "FISH_COUNT", B.FISH_NAME
from FISH_INFO as A
    join FISH_NAME_INFO as B
        on A.FISH_TYPE = B.FISH_TYPE
# where A.LENGTH is not null
Group by FISH_NAME
order by FISH_COUNT desc  
"""