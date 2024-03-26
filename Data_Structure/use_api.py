import json
d={"name": "start,시작"}
# json 문자열 변환 및 ensure_ascii=False : 한글 포함이라 그대로 가져오기 위해서이다
d_convert=json.dumps(d, ensure_ascii=False)

print(d)

print(type(d_convert))

# 문자열을 파이썬 객체 변환

d2=json.loads(d_convert)

print(type(d2))