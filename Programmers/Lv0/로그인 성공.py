"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120883
"""
#풀이1
def solution(id_pw, db):
    for a, b in db:
        if a == id_pw[0] and b == id_pw[1]:
            return "login"
        elif a == id_pw[0] and not b == id_pw[1]:
            return "wrong pw"
        else:
            continue
    return "fail"

#풀이2

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
