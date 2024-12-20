"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/276013
"""

# 풀이 과정
"""
select ID,EMAIL,FIRST_NAME,LAST_NAME
    from DEVELOPER_INFOS
    where  SKILL_1 = "Python" or SKILL_2 = "Python" or SKILL_3 = "Python"
    order by ID asc;
    """
