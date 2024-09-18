"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42893
"""
# 내 풀이(개선 중)
"""
조건:
기본점수: 검색어가 등장하는 횟수
외부링크 수:다른 외부 페이지와 연결된 개수 
링크점수:기본점수/외부링크 수 총합

한 웹페이지의 링크점수는 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합이다.
"""
from collections import defaultdict
from collections import deque


def solution(word, pages):
    new = []
    word = word.upper()
    english = set(list("abcdefhijklmnopqrstuvwxyz".upper()))

    # 페이지 모두 대문자로 변환
    for p in pages:
        n = p.upper()
        new.append(n)

    # 기본점수, 외부 링크점수
    check = [[0] * 2 for i in range(len(new))]

    # 웹페이지별 구분
    linkpage = []

    # 내부 링크 구분 및 링크 정리 > linkpage
    for n in range(len(new)):
        check[n][1] = new[n].count("<A HREF")

        l = new[n].split(" ")

        for f in l:
            if "CONTENT=" in f:
                start = ''
                link_page = deque(list(f))
                while link_page:
                    k = link_page.popleft()
                    if k == "\"":
                        while True:
                            s = link_page.popleft()
                            if s == "\"":
                                break
                            else:
                                start += s
                linkpage.append(start)
    # 링크 점수
    check_list = [0] * len(pages)

    # 기본 점수
    for count, i in enumerate(new):
        num = 0
        start = ""
        for eng in list(i):
            if eng in english:
                start += eng
            else:
                if start == word:
                    num += 1
                    start = ""

                else:
                    start = ""

        check[count][0] = num

    # 링크 점수
    for my in range(len(pages)):
        for another in range(len(pages)):
            if my != another and linkpage[another] in (pages[my]).upper():
                # print("또 다른 곳",linkpage[another],"check page",my,linkpage[my])
                # 링크점수 해당 링크 기본점수 / 외부링크 수
                if check[my][1] != 0:
                    check_list[another] += check[my][0] / check[my][1]

    result = []
    # print(check,"기본 점수, 외부 링크 수")
    # print(check_list,"링크 점수")

    for r in range(len(check_list)):
        result.append(check[r][0] + check_list[r])

    # print(result,"결과")

    return result.index(max(result))ㄴ
# 내 풀이(개선 중)
"""
조건:
기본점수: 검색어가 등장하는 횟수
외부링크 수:다른 외부 페이지와 연결된 개수 
링크점수:기본점수/외부링크 수 총합

한 웹페이지의 링크점수는 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합이다.
"""
from collections import defaultdict
from collections import deque


def solution(word, pages):
    new = []
    word = word.upper()
    english = set(list("abcdefhijklmnopqrstuvwxyz".upper()))

    # 페이지 모두 대문자로 변환
    for p in pages:
        n = p.upper()
        new.append(n)

    # 기본점수, 외부 링크점수
    check = [[0] * 2 for i in range(len(new))]

    # 웹페이지별 구분
    linkpage = []

    # 내부 링크 구분 및 링크 정리 > linkpage
    for n in range(len(new)):
        check[n][1] = new[n].count("<A HREF")

        l = new[n].split(" ")

        for f in l:
            if "CONTENT=" in f:
                start = ''
                link_page = deque(list(f))
                while link_page:
                    k = link_page.popleft()
                    if k == "\"":
                        while True:
                            s = link_page.popleft()
                            if s == "\"":
                                break
                            else:
                                start += s
                linkpage.append(start)

    # 링크 점수
    check_list = [0] * len(pages)

    # 기본 점수
    for count, i in enumerate(new):
        num = 0
        start = ""
        for eng in list(i):
            if eng in english:
                start += eng
            else:
                if start == word:
                    num += 1
                    start = ""

                else:
                    start = ""

        check[count][0] = num

    # 링크 점수
    for my in range(len(pages)):
        for another in range(len(pages)):
            if my != another and linkpage[another] in (pages[my]).upper():
                print("또 다른 곳", linkpage[another], "check page", my, linkpage[my])
                # 링크점수 해당 링크 기본점수 / 외부링크 수
                if check[my][1] != 0:
                    check_list[another] += check[my][0] / check[my][1]

    result = []
    # print(check,"기본 점수, 외부 링크 수")
    # print(check_list,"링크 점수")

    for r in range(len(check_list)):
        result.append(check[r][0] + check_list[r])

    # print(result,"결과")

    return result.index(max(result))

# 내 풀이(개선 중)
"""
조건:
기본점수: 검색어가 등장하는 횟수
외부링크 수:다른 외부 페이지와 연결된 개수 
링크점수:기본점수/외부링크 수 총합
"""

def solution(word, pages):
    new = []
    word = word.upper()

    for p in pages:
        n = p.upper()

        new.append(n)

    check = [[0] * 3 for i in range(len(new))]

    for n in range(len(new)):
        check[n][1] = new[n].count("<A HREF")

        l = new[n].split(" ")

        for f in l:
            if f == word:
                check[n][0] += 1

    answer = 0
    return answer

# 다른 사람 풀이
from operator import indexOf
import re


def solution(word, pages):
    pages_info = []
    for i, page in enumerate(pages):
        temp = list(seperate(word, page)) + [0, i]
        pages_info.append(temp)
    for page in pages_info:
        url, basic_score, link_num, links, link_score, index = page
        for link in links:
            for page in pages_info:
                if link == page[0]:
                    page[4] += basic_score / link_num
    pages_info.sort(key=lambda x: -(x[1]+x[4]))
    return pages_info[0][5]


def seperate(word, page):
    basic_score = 0
    for f in re.findall(r'[a-zA-Z]+', page.lower()):
        if f == word.lower():
            basic_score += 1
    url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
    external_links = re.findall('<a href="(https://[\S]*)"', page)
    external_links_num = len(external_links)

    return url, basic_score, external_links_num, external_links