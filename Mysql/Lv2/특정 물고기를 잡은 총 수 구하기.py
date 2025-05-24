"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/298518
"""

# 풀이 과정
"""
select count(*) "FISH_COUNT"
from FISH_INFO as A
    join FISH_NAME_INFO as B
    on A.FISH_TYPE = B.FISH_TYPE
where B.FISH_NAME in ('BASS','SNAPPER')
    # and LENGTH is not null
"""

# 다른 사람 풀이
"""
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE FISH_TYPE IN (
    SELECT FISH_TYPE FROM FISH_NAME_INFO
    WHERE FISH_NAME IN ('BASS', 'SNAPPER')
);
"""