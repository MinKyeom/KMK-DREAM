"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/293260
"""

# 풀이 과정

"""

select count(TIME) "FISH_COUNT",month(TIME) "MONTH"
from FISH_INFO
# where LENGTH >=10
Group by month(TIME)
order by month(TIME)

"""