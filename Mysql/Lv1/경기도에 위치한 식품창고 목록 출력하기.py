"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/131114
"""

"""
SELECT
    WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
        CASE
            when FREEZER_YN is not null then FREEZER_YN

        else "N"

        END
        "FREEZER_YN"

from FOOD_WAREHOUSE
"""