"""
완전 탐색
전체 경우의 수를 봐야하는 문제이다
"""

discounts = [10, 20, 30, 40]
answer = [-1, -1]


def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discount_list = [0] * m

    def search(idx):
        global answer
        if idx == m:
            # print(idx,discount_list)
            sale_num, cost_num = 0, 0
            for i in range(n):
                tmp = 0
                for j in range(m):
                    if users[i][0] <= discount_list[j]:
                        tmp += emoticons[j] * (100 - discount_list[j]) // 100
                if tmp >= users[i][1]:
                    sale_num += 1
                else:
                    cost_num += tmp
            if sale_num > answer[0] or sale_num == answer[0] and cost_num > answer[1]:
                answer = [sale_num, cost_num]
                # print(answer)
            return

        for i in range(4):
            discount_list[idx] = discounts[i]
            # print(idx,discount_list,"check")
            search(idx + 1)

    print("확인")
    search(0)  # 재귀함수 start, dfs풀이 중 하나
    print(answer)
    return answer
