"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/132203
"""

"""
SELECT DR_NAME,DR_ID,MCDP_CD,DATE_FORMAT(HIRE_YMD,"%Y-%m-%d") "HIRE_YMD"

from DOCTOR

where MCDP_CD in ("CS","GS")

order by HIRE_YMD desc, DR_NAME asc
"""