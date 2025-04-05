"""
출처:프로그래머스.
https://school.programmers.co.kr/learn/courses/30/lessons/132201
"""

"""
SELECT PT_NAME,PT_NO,GEND_CD,AGE,
    CASE 
        when TLNO is not null then TLNO
        
        else "NONE"
        
    END "TLNO"

from PATIENT

where GEND_CD="W" and AGE <=12

order by AGE desc, PT_NAME asc
"""