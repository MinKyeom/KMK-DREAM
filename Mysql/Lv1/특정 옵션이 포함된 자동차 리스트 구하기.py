"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/157343
"""

# 풀이 과정
"""
select *

from CAR_RENTAL_COMPANY_CAR

# %를 통하여 앞뒤로 네비게이션이 들어간 목록을 찾는다
where OPTIONS like "%네비게이션%"

order by CAR_ID desc
"""