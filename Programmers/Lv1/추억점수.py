# 내 풀이
def solution(name, yearning, photo):
    count = 0
    result = []
    for a in range(len(photo)):
        for b in range(len(photo[a])):
            for c in range(len(name)):
                if photo[a][b] == name[c]:
                    count += yearning[c]
                else:
                    continue
        result.append(count)
        count = 0

    return result

# 다른 사람 풀이
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]