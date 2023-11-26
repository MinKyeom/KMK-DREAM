# 내 풀이
def solution(s):
    result = s

    if len(s) % 2 == 1:
        k = int(len(s) / 2) + 1
    else:
        k = int(len(s) / 2) + 1

    for a in range(1, k):
        check = ""
        count = 1
        before = s[0:a]
        flag = False

        #         if 2*a>=len(s):
        #             continue

        for b in range(a, len(s), a):
            if b + a > len(s):
                if count >= 2:
                    check = check + str(count) + before + s[b:]
                    flag = True
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
                check = check + str(count) + before
            else:
                check = check + before

        # print(check,flag,len(check),a)
        if len(check) < len(result):
            result = check

    return len(result)

# 다른 사람 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))