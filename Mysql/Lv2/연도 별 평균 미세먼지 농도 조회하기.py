"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/284530
"""

# 풀이과정
"""
select year(YM) "year",round(avg(PM_VAL1),2) "PM10",round(avg(PM_VAL2),2) "PM2.5"
from AIR_POLLUTION
group by year(YM),location2
having location2 = "수원"
order by year asc 
"""