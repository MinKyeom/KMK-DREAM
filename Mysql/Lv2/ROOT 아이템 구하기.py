"""
출처:프로그래머스, 
https://school.programmers.co.kr/learn/courses/30/lessons/273710
"""

# 풀이 과정 
"""
select B.ITEM_ID,A.ITEM_NAME
from ITEM_INFO as A,ITEM_TREE as B
where 1=1
    and A.ITEM_ID = B.ITEM_ID
    and B.PARENT_ITEM_ID is null
order by ITEM_ID asc 
"""