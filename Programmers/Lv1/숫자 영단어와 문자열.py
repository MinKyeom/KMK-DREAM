# 내 풀이
def solution(s):
    num=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for x in range(len(num)):
        s=s.replace(num[x],str(x))
    return int(s)

# 다른 사람 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)