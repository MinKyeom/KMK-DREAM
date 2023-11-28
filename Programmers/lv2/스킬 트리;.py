# 내 풀이
def solution(skill, skill_trees):
    before = list(skill)

    result = 0

    for a in skill_trees:

        check = []

        for b in list(a):
            flag = False

            if b not in before:
                continue

            else:
                t = before.index(b)

                if t == 0:
                    check.append(b)

                else:
                    for c in range(t):
                        if before[c] in check:
                            continue
                        else:
                            flag = True
                            break

                    if flag == True:
                        break
                    else:
                        check.append(b)

        if flag == False:
            result += 1

    return result

# 다른 사람 풀이

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
