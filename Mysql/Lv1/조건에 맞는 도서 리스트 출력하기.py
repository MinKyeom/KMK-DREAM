"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/144853
"""

"""
SELECT BOOK_ID,date_format(PUBLISHED_DATE,'%Y-%m-%d') "PUBLISHED_DATE"

from book

where PUBLISHED_DATE like "2021%" and CATEGORY like "인문"

order by PUBLISHED_DATE asc
"""