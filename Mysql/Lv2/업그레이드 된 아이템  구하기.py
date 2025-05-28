"""
출처:프로그래머스, 
https://school.programmers.co.kr/learn/courses/30/lessons/273711
"""
# 풀이 과정
"""
-- 새로운 테이블의 형태를 조인해서 변환시킨 아이템 id의 이름을 가져오는 방향성 고민 
# select A.ITEM_ID "ITEM_ID",B.ITEM_NAME,B.RARITY,B.ITEM_ID
# from ITEM_TREE AS A,
#     (select *
#     from ITEM_INFO  
#     where RARITY = "RARE") AS B
# where B.ITEM_ID = A.PARENT_ITEM_ID
# order by A.ITEM_ID desc

select C.ITEM_ID,C.ITEM_NAME,C.RARITY
from ITEM_INFO AS D,
(select B.ITEM_ID,B.PARENT_ITEM_ID,A.RARITY,A.ITEM_NAME
from ITEM_INFO AS A, ITEM_TREE AS B
where B.ITEM_ID = A.ITEM_ID) AS C
where 1=1
and D.ITEM_ID = C.PARENT_ITEM_ID
and D.RARITY = "RARE"
order by ITEM_ID desc
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