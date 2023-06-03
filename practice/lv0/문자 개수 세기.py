# 내 풀이
def solution(my_string):
    english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    result = []
    english = "".join(english).upper()
    print(my_string.count("a"))
    for x in list(english):
        result.append(my_string.count(x))
    english = "".join(english).lower()
    for y in list(english):
        result.append(my_string.count(y))

    return result


# 다른 사람 풀이

def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer

