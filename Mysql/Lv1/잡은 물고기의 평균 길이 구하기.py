"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/293259
"""

# 풀이 과정

"""
select round(avg(nw),2) "AVERAGE_LENGTH"
    from (select LENGTH,
            CASE
                when LENGTH >=10 then
                    LENGTH
                else 10
            end as nw
            from FISH_INFO ) new
"""