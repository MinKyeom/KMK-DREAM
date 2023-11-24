# 내 풀이(개선 중)
def solution(s):
    result = s
    k = 0
    for a in range(1, int(len(s) / 2) + 1):
        check = ""
        before = s[0:a]
        count = 1
        flag = False

        for b in range(a, len(s), a):
            if b + a > len(s):
                if count >= 2:
                    check = check + str(count) + before + s[b:]
                else:
                    check = check + s[b:]

                falg = True
                break

            after = s[b:b + a]

            if after == before:
                count += 1
                before = after

            else:
                if count >= 2:
                    check = check + str(count) + before
                    before = after
                    count = 1
                else:
                    check = check + before
                    before = after

        if flag == False:
            if count >= 2:
                check = check + str(count) + after
            else:
                check = check + after

        # print(check)

        if len(check) < len(result):
            result = check
            k = a
    print(k, result, flag)
    return len(result)