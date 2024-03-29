import json
d={"name": "start,시작"}
# json 문자열 변환 및 ensure_ascii=False : 한글 포함이라 그대로 가져오기 위해서이다
d_convert=json.dumps(d, ensure_ascii=False)

print(d)

print(type(d_convert))

# 문자열을 파이썬 객체 변환

d2=json.loads(d_convert)

print(type(d2))

# 괄호에 따른 기본 변환 과정 다시 체크
d3=json.loads('{"name": "min" }')

print(d3)

import pandas as pd

d4_str = """
[
  {"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name": "혼자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""
d4 = json.loads(d4_str)


import pandas as pd
import io
d4=io.StringIO(d4_str)

pd.read_json((d4))
print(d4,"new")
pd.DataFrame(d4)
print(d4)


