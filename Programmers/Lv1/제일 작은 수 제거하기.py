# 내 풀이
def solution(arr):
    k=min(arr)
    a=arr.remove(k)
    return arr if len(arr)>=1 else [-1]

# 다른 사람 풀이
def rm_small(mylist):
    # 함수를 완성하세요
    return [i for i in mylist if i > min(mylist)]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
