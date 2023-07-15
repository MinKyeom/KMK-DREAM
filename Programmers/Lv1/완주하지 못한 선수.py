# 내 풀이
def solution(participant, completion):
    if len(set(participant) - set(completion)) == 1:
        k = set(participant) - set(completion)
        k = list(k)
        return "".join(k)

    else:
        participant.sort()
        completion.sort()
        for x in range(len(completion)):
            if participant[x] == completion[x]:
                continue
            else:
                return participant[x]
        return participant[len(participant) - 1]

# 다른 사람 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
