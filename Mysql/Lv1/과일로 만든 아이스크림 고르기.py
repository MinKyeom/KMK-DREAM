"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/133025
"""

"""
풀이 과정

SELECT FIRST_HALF.FLAVOR "FLAVOR"

from FIRST_HALF
    inner join ICECREAM_INFO
    on  FIRST_HALF.FLAVOR=ICECREAM_INFO.FLAVOR
    
where FIRST_HALF.TOTAL_ORDER >3000 and ICECREAM_INFO.INGREDIENT_TYPE="fruit_based"

order by FIRST_HALF.TOTAL_ORDER desc
"""