"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/284531
"""

# 풀이과정_개선 중
"""
select ROUTE,
    round( sum(D_BETWEEN_DIST),2 ) "TOTAL_DISTANCE",
    round(avg(D_BETWEEN_DIST),3) "AVERAGE_DISTANCE" 
from SUBWAY_DISTANCE
group by ROUTE
"""

