"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/298515
"""

# 풀이 과정
"""
select CONCAT(LENGTH,"cm") 'MAX_LENGTH'
    from FISH_INFO
    order by LENGTH desc
    limit 1
"""