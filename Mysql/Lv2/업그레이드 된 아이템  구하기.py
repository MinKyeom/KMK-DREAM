"""
출처:프로그래머스, 
https://school.programmers.co.kr/learn/courses/30/lessons/273711
"""

# 풀이과정 개선 중
"""
-- 새로운 테이블의 형태를 조인해서 변환시킨 아이템 id의 이름을 가져오는 방향성 고민 
select * -- A.ITEM_ID,A.ITEM_NAME,B.RARITY
from ITEM_TREE AS A,
    (select *
    from ITEM_INFO  
    where RARITY = "RARE") AS B
where B.ITEM_ID = A.PARENT_ITEM_ID
-- order by ITEM_ID desc

"""