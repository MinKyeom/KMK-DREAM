# 내 풀이
def solution(today, terms, privacies):
    today = list(map(int, today.split(".")))
    c_t = (today[0] * 12 * 28) + (today[1] * 28) + (today[2])
    terms_list = []
    result = []
    for x in terms:
        k = x.split(" ")
        terms_list.append(k[0])
        terms_list.append(int(k[1]))
    count = 1
    for y in privacies:
        z = y.split(" ")
        eng_type = z[1]
        f = terms_list.index(z[1])
        plus = int(terms_list[f + 1]) * 28
        day = list(map(int, z[0].split(".")))
        print(day)
        check = (day[0] * 12 * 28) + (day[1] * 28) + day[2] + plus  # 만기일

        if check <= c_t:
            print(1)
            result.append(count)
            count += 1
            continue
        else:
            count += 1
            continue

    return result
# 다른 사람 풀이
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
