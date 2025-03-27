"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/151138
"""

"""

풀이 과정

select HISTORY_ID,CAR_ID,Date_format(START_DATE,"%Y-%m-%d") "START_DATE",Date_format(END_DATE,"%Y-%m-%d") "END_DATE",
    CASE 
        when datediff(END_DATE,	START_DATE) >= 29 then "장기 대여"
        
        else "단기 대여"
        
    END "RENT_TYPE"

from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE Like "2022-09%"
order by HISTORY_ID desc

"""