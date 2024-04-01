# xml 문자열을 파이썬 객체로 변환하기:fromstring()

x_str="""
<cal>
    <cals> 이건 </cals>
    <year> 2024 </year>
    <month> 4 </month>
    <day> 1 </day>
</cal>
"""

import xml.etree.ElementTree as et

check=et.fromstring(x_str)

print(type(check))

print(check.tag)

# 자식 엘리먼트 확인하기

cal_son=list(check)
print(cal_son)

#year, month, day= cal_son

#print(year.text)
#print(month.text)


# findtext # 텍스트로 자식 엘리먼트 찾기
year_find=check.findtext("cals")
print(year_find)

#notepad++로 html작성하면서 체크 해보기